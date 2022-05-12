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
import textwrap
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
        data_graph = self.generate_shacl_data_graph(data)
        if self.validate_data_integrity(data_graph=data_graph, data_hash=self.get_hash(data)):
            if "temperature" in data['observedproperty']:
                shacl_graph = SHACLShapes().temperature()
            elif "humidity" in data['observedproperty']:
                shacl_graph = SHACLShapes().relative_humidity()
            return self.validate_data_quality(data_graph=data_graph, shacl_graph=shacl_graph)
        else:
            return False



    def validate_data_quality(self, data_graph, shacl_graph):
        data_graph = data_graph.serialize(format="turtle")
        conforms, report, message = validate(data_graph, shacl_graph=shacl_graph, advanced=True, debug=False)
        return conforms

    def validate_data_integrity(self, data_graph, data_hash):
        query = textwrap.dedent("""
              ASK {{
            ?s a sosa:Observation.
            FILTER EXISTS {{?s sricats:hasHash ?o
                FILTER (?o = "{0}"^^xsd:string)}}
            }}""").format(data_hash)
        qres = data_graph.query(query)
        return bool(list(qres)[0])

    def get_hash(self, data):
        extractTimeStamp = datetime.strptime(data["resultobservationtime"], '%Y-%m-%dT%H:%M:%S:%f')
        return hashlib.sha256(bytes(str(int(extractTimeStamp.strftime("%Y%m%d%M%S%f")) + data["observationresult"]), 'utf-8')).hexdigest()