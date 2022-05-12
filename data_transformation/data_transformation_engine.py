# -*- coding: utf-8 -*-
# @Time    : 23.01.22 23:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_transformation_engine.py
# @Software: PyCharm
import sys


import textwrap
class DataTransformationEngine:

    def get_unit(self, data):
        if "temperature" in data['observedproperty']:
            return "om:degreeCelsius"
        elif "humidity" in data['observedproperty']:
            return "om:percent"
    def transform(self, data):
        if type(data) != dict:
            raise TypeError("Data should be of type dictionary")
        transformed_data = textwrap.dedent("""
                :observation\/{4} a sosa:Observation;
                sosa:hasSimpleResult :{1} ;
                sosa:madeBySensor :sensor\/{0} ;
                sosa:resultTime :{2};
                :hasHash :{5};
                om:hasUnit :{6};
                sosa:observedProperty :{3} .
                :sensor\/{0} a sosa:Sensor ;
                sosa:observes :observation\/{4} .
        """).format(
                    data["observationsensorid"],
                    data["observationresult"],
                    data["resultobservationtime"],
                    data["observedproperty"],
                    data["observationid"],
                    data["hashvalue"],
                    self.get_unit(data=data)
                   )

        return transformed_data