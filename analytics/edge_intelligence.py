# -*- coding: utf-8 -*-
# @Time    : 12.05.22 21:49
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : edge_intelligence.py
# @Software: PyCharm
from owlready2 import *
from analytics.rules import Rules

class EdgeIntelligence:
    def get_name_space(self):
        onto_sensor = get_ontology("http://www.tekrajchhetri.com/sricats")
        sensor_namespace = onto_sensor.get_namespace("http://www.w3.org/ns/sosa")
        measurement_unit_namespace = onto_sensor.get_namespace(
            "http://www.ontology-of-units-of-measure.org/resource/om-2")
        return [onto_sensor,sensor_namespace,measurement_unit_namespace]


    def load_ontology(self):
        return get_ontology("ontology_sricats.owl").load()

    def perform_reasoning(self, type, value):
        onto = self.load_ontology()
        onto_sensor, sensor_namespace, measurement_unit_namespace = self.get_name_space()
        with onto:
            rules = Imp()
            rules.set_as_rule(Rules().get_swrl_rules()[type], namespaces=[onto_sensor,
                                                                                         sensor_namespace,
                                                                                         measurement_unit_namespace])
        reasoning = sensor_namespace.Observation(hasSimpleResult=value)

        sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
        return  self.reasoning_result(reasoning.is_a)


    def reasoning_result(self, result):
        if len(result) == 2:
            return {"alert":str(result[1]).split(".")[1]}
        else:
            return {"alert":"None"}

if __name__ == '__main__':
    e  = EdgeIntelligence()
    print(e.perform_reasoning("humidity",110.0))