# -*- coding: utf-8 -*-
# @Time    : 15.03.22 21:35
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : validation_engine.py
# @Software: PyCharm
from helper import Helpers
from shacl_shapes import SHACLShapes
from pyshacl import validate
from rdflib import Graph
class ValidationEngine(Helpers):
    def data_quality_validation(self, data):
        """ perform validation of the received input data for quality
        :param sensor data
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

        data_graph = data_graph.serialize(format="turtle") #Graph().parse(data=data_graph, format="turtle")
        print(data_graph)
        if "temperature" in data['observedproperty']:
            shape_graph = SHACLShapes().temperature()
        elif "humidity" in data['observedproperty']:
            shape_graph = SHACLShapes().relative_humidity()
        conforms, report, message = validate(data_graph, shacl_graph=shape_graph, advanced=True, debug=False)
        print(message)
        return conforms

    def data_integrity_validator(self, input_rdf):
        """ Performs integrity checks of the data to ensure no data tampering is done
        :param input_rdf: input data in RDF format
        :return:
        """
        return False

# if __name__ == '__main__':
#     v = ValidationEngine()
#     data = {'observedproperty': 'STI_W201_humidity',
#             'observationsensorid': 'DS18B20',
#             'observationresult': 88.6,
#             'resultobservationtime': "2005-02-28T00:00:00",
#             'observationid': f'DS18B20_DS18B20_asfasdf',
#             'hashvalue': "c38f83392718b1024aff70b5fd0d79fdc04ee55fba7458554e6326f8b08bdf42"
#             }
#
#     print(v.data_quality_validation(data))