# -*- coding: utf-8 -*-
# @Time    : 23.01.22 23:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_transformation_engine.py
# @Software: PyCharm
import sys
from rdflib import Graph, Literal, XSD, RDF,URIRef
from rdflib import Namespace

class DataTransformationEngine:
    def generate_shacl_data_graph(self, data):
        SRICATS = Namespace("http://www.tekrajchhetri.com/sricats/")
        SOSA = Namespace("http://www.w3.org/ns/sosa/")
        OM = Namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")
        g = Graph()
        g.bind('sosa', SOSA)
        g.bind('sricats', SRICATS)
        g.bind('om', OM)
        sensor = URIRef(f"{SOSA['Sensor']}/{data['observationsensorid']}")
        obs = URIRef(f"{SOSA['Observation']}/{data['observationid']}")
        g.add((sensor, RDF.type, SOSA['Sensor']))
        g.add((sensor, SOSA["observes"], obs))
        g.add((obs, RDF.type, SOSA['Observation']))
        g.add((obs, SOSA['madeBySensor'], sensor))
        g.add((obs, SOSA['observedProperty'], URIRef(f"{SOSA['observedProperty']}/{data['observedproperty']}")))
        g.add((obs, SOSA['hasSimpleResult'], Literal(data['observationresult'], datatype=XSD.double)))
        g.add((obs, SOSA['resultTime'], Literal(data['resultobservationtime'], datatype=XSD.dateTime)))
        if "temperature" in data['observedproperty']:
            g.add((obs, OM['hasUnit'], OM["degreeCelsius"]))
        elif "humidity" in data['observedproperty']:
            g.add((obs, OM['hasUnit'], OM["percent"]))
        g.add((obs, SRICATS['hasHash'], Literal(data['hashvalue'], datatype=XSD.string)))
        return g

    def transform(self, rdf_data):
        transformed_data = ""
        for subject, predicate, obj in rdf_data:
            transformed_data = transformed_data + subject.n3() + " " + predicate.n3() + " " + obj.n3() + " . \n"

        return transformed_data