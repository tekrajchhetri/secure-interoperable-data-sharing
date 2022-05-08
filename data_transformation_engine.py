# -*- coding: utf-8 -*-
# @Time    : 23.01.22 23:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_transformation_engine.py
# @Software: PyCharm
import sys

from data_migration import DataMigration
import textwrap
import json
class DataTransformationEngine:

    def transform(self, data):
        data = json.loads(data)
        if type(data) != dict:
            raise TypeError("Data should be of type dictionary")
        transformed_data = textwrap.dedent("""
                :observation\/{4} a sosa:Observation;
                sosa:hasSimpleResult :{1} ;
                sosa:madeBySensor :sensor\/{0} ;
                sosa:resultTime :{2};
                :hasHash :{5};
                sosa:observedProperty :{3} .
                :sensor\/{0} a sosa:Sensor ;
                sosa:observes :observation\/{4} .
        """).format(
                    data["observationsensorid"],
                    data["observationresult"],
                    data["resultobservationtime"],
                    data["observedproperty"],
                    data["observationid"],
                    data["hashvalue"]
                   )
        dm = DataMigration()
        status = dm.migrate_to_gdb(transformed_data)
        sys.stdout.write(status)
