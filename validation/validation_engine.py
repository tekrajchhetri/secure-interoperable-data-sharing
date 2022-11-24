# -*- coding: utf-8 -*-
# @Time    : 15.03.22 21:35
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : validation_engine.py
# @Software: PyCharm
from helper.helper import Helpers
from validation.shacl_shapes import SHACLShapes
from pyshacl import validate
from datetime import datetime
import hashlib
from rdflib import Graph
import textwrap
from smart_contract.transaction import Transaction
from data_transformation.data_transformation_engine import DataTransformationEngine
class ValidationEngine(Helpers):
    def validate(self, data):
        """ perform validation of the received input data
           1. Integirty validation
           2. Quality validation
        :param  data
        Example
            {'observedproperty': 'STI_W201_humidity',
            'observationsensorid': 'DS18B20',
            'observationresult': 88.6,
            'resultobservationtime': "2005-02-28T00:00:00",
            'observationid': f'DS18B20_DS18B20_asfasdf',
            'hashvalue': "c38f83392718b1024aff70b5fd0d79fdc04ee55fba7458554e6326f8b08bdf42"
            }
        :return: boolean
        """
        data_graph_v = DataTransformationEngine().parse_kg_data_to_turtle(data)
        if self.validate_data_integrity(data_graph=data_graph_v, data_hash=self.get_hash(data_graph_v)):
            print("##########################################################################################")
            print("######################  Integrity Verified, Proceeding to Next steps #####################")
            print("##########################################################################################")
            if "temperature" in self.get_type(data_graph_v).lower():
                shacl_graph_v = SHACLShapes().temperature()
            elif "humidity" in self.get_type(data_graph_v).lower():
                shacl_graph_v = SHACLShapes().relative_humidity()
            if self.validate_data_quality(data_graph_v=data_graph_v, shacl_graph_v=shacl_graph_v):
                return {"status":True, "rdf_turtle_data":data_graph_v}
            else:
                return {"status": False}
        else:
            return {"status": False}

    def turtle_str_to_rdf_graph(self, tutle_data_str):
        return Graph().parse(data=tutle_data_str)

    def validate_data_quality(self, data_graph_v, shacl_graph_v):
        data_graph_v = data_graph_v
        conforms, report, message = validate(data_graph=data_graph_v, shacl_graph=shacl_graph_v, advanced=True, debug=False)
        return conforms

    def validate_data_integrity(self, data_graph, data_hash):
        g = Graph().parse(data=data_graph)
        queryr = textwrap.dedent("""
              ASK {{
            ?s a sosa:Observation.
            FILTER EXISTS {{?s sricats:hasHash ?o
                FILTER (?o = "{0}"^^xsd:string)}}
            }}""").format(data_hash)
        qres = g.query(queryr)
        return bool(list(qres)[0])

    def get_type(self, data_graph):
        g = Graph().parse(data=data_graph)
        queryr = textwrap.dedent("""
                SELECT  ?o WHERE {{
                ?s a sosa:Observation;
                   sosa:observedProperty ?o.
            }}""")
        qres = g.query(queryr)
        for row in qres:
            return  row.o

    def get_blockchainHashInformation(self, data_graph):
        g = Graph().parse(data=data_graph)
        queryr = textwrap.dedent("""
                SELECT  ?o WHERE {{
                ?s a sosa:Observation;
                   sricats:hasBlockChainHash ?o.
            }}""")
        qres = g.query(queryr)
        print(list(qres))

        for row in qres:
            return  row.o

    def get_data_val(self, data_graph, objectProperty):
        g = Graph().parse(data=data_graph)
        queryr = textwrap.dedent("""
                SELECT  ?o WHERE {{
                ?s a sosa:Observation;
                   {0} ?o.
            }}""").format(objectProperty)
        qres = g.query(queryr)
        for row in qres:
            return  row.o

    def get_observationid_and_sensor(self, data_graph, returnSorO):
        g = Graph().parse(data=data_graph)
        queryr = textwrap.dedent("""
                SELECT  ?{0} WHERE {{
                ?s a sosa:Sensor;
                   sosa:observes ?o.
            }}""").format(returnSorO)
        qres = g.query(queryr)
        print(queryr, qres)
        for row in qres:
            return  row.o if returnSorO == "o" else row.s

    def get_hash(self, data_graph):
        blockchainHash = self.get_blockchainHashInformation(data_graph)

        if blockchainHash is None:
            return None
        else:
            return Transaction().decode_data(blockchainHash)