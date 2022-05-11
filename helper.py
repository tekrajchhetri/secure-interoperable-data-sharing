# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : helper.py
# @Software: PyCharm
import yaml
from yaml.loader import SafeLoader
import  sys
from rdflib import Graph, Literal, XSD, RDF,URIRef
from rdflib import Namespace

class Helpers:

    def read_yml(self, filename):
        # Open the file and load the file
        try:
            with open(filename) as f:
                data = yaml.load(f, Loader=SafeLoader)
            return data
        except FileNotFoundError as e:
            sys.stderr.write("File not found")

    def get_rabbit_config_details(self):
        details = self.read_yml("config.yml")
        return {"username":details["rabbitdetails"][0]["username"][0],
                "password":details["rabbitdetails"][1]["password"][0],
                "hostname": details["rabbitdetails"][2]["host"][0],
                "topic": details["rabbitdetails"][3]["topic"][0],
                "port": details["rabbitdetails"][4]["port"][0],
                "exchange": details["rabbitdetails"][5]["exchange"][0],
                "queuename": details["rabbitdetails"][6]["queuename"][0]
                }

    def get_gdb_config_details(self):
        details = self.read_yml("config.yml")
        return {"username":details["graphdbdetails"][0]["username"][0],
                "password":details["graphdbdetails"][1]["password"][0],
                "hostname": details["graphdbdetails"][2]["host"][0],
                "repository": details["graphdbdetails"][3]["repository"][0]
                }


    def generate_shacl_data_graph(self, data):
        SRICATS = Namespace("http://www.tekrajchhetri.com/sricats/")
        SOSA = Namespace("http://www.w3.org/ns/sosa/")
        OM = Namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")
        g = Graph()
        g.bind('sosa', SOSA)
        g.bind('sricats', SRICATS)
        g.bind('om', OM)
        sensor = URIRef(f"sensor/{data['observationsensorid']}")
        obs = URIRef(f"observation/{data['observationid']}")
        g.add((sensor, RDF.type, SOSA['Sensor']))
        g.add((sensor, SOSA["observes"], obs))
        g.add((obs, RDF.type, SOSA['Observation']))
        g.add((obs, SOSA['madeBySensor'], sensor))
        g.add((obs, SOSA['observedProperty'], URIRef(data['observedproperty'])))
        g.add((obs, SOSA['hasSimpleResult'], Literal(data['observationresult'], datatype=XSD.double)))
        g.add((obs, SOSA['resultTime'], Literal(data['resultobservationtime'], datatype=XSD.dateTime)))
        if "temperature" in data['observedproperty']:
            g.add((obs, OM['hasUnit'], OM["degreeCelsius"]))
        elif "humidity" in data['observedproperty']:
            g.add((obs, OM['hasUnit'], OM["percent"]))
        g.add((obs, SRICATS['hasHash'], Literal(data['hashvalue'], datatype=XSD.string)))
        return g