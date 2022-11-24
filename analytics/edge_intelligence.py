# -*- coding: utf-8 -*-
# @Time    : 12.05.22 21:49
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : edge_intelligence.py
# @Software: PyCharm
from owlready2 import *
from analytics.rules import Rules
from data_migrator.Publish import Publish
from validation.validation_engine import ValidationEngine
from data_transformation.data_transformation_engine import DataTransformationEngine
import json
import textwrap
class EdgeIntelligence:
    def get_name_space(self):
        onto_sensor = get_ontology("http://www.tekrajchhetri.com/sricats")
        sensor_namespace = onto_sensor.get_namespace("http://www.w3.org/ns/sosa")
        measurement_unit_namespace = onto_sensor.get_namespace(
            "http://www.ontology-of-units-of-measure.org/resource/om-2")
        return [onto_sensor,sensor_namespace,measurement_unit_namespace]


    def load_ontology(self):
        return get_ontology("core/ontology_sricats.owl").load()

    def reasoning(self, value, rtype):
        onto = self.load_ontology()
        onto_sensor, sensor_namespace, measurement_unit_namespace = self.get_name_space()
        with onto:
            rules = Imp()
            rules.set_as_rule(Rules().get_swrl_rules()[rtype], namespaces=[onto_sensor,
                                                                          sensor_namespace,
                                                                          measurement_unit_namespace])
            reasoning = sensor_namespace.Observation(hasSimpleResult=value, hasedgeReasoningType=rtype)
            t = sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
            return  self.reasoning_result(reasoning.is_a,rtype)


    def reasoning_result(self, result,rtype):
        key = f"alert"
        if len(result) == 2:

            return {key:str(result[1]).split(".")[1]}
        else:
            return {key:"None"}


    def start_edge_intelligence(self, data, mode):
        """ Starts the analytics
        :param data: Published Sensor data
        :param mode: what mode reasoning is running
        :edge - returns result immediately
        :fog - publishes the result to a topic defined in config file
        :return: dict
        """
        data = DataTransformationEngine().parse_kg_data_to_turtle(data)
        print("##########################################################################################")
        print(f"######################            DEBUG  EDGE INT                   #####################")
        print(f"######################            {data, type(data)}                #####################")
        print("##########################################################################################")
        print(ValidationEngine().get_data_val(data,"sosa:hasSimpleResult"))
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if "temperature" in ValidationEngine().get_type(data).lower():
            rtype = "temperature"

        if "humidity" in ValidationEngine().get_type(data).lower():
            rtype="humidity"
        if mode=="fog":
            # for resource constraint devices
            owlready2.reasoning.JAVA_MEMORY=4800

        result = self.reasoning(value=float(ValidationEngine().get_data_val(data, "sosa:hasSimpleResult")),rtype=rtype)
        print("##########################################################################################")
        print(f"######################            RESULT                          #####################")
        print(f"######################            {result}                          #####################")
        print("##########################################################################################")

        result["observationsensorid"] = ValidationEngine().get_observationid_and_sensor(data, "s")
        result["observedproperty"] = ValidationEngine().get_data_val(data,"sosa:observedproperty")
        result["observationid"] = ValidationEngine().get_observationid_and_sensor(data, "o")
        if mode == "edge":
            return result
        else:
            print("##########################################################################################")
            print(f"######################  Preparing to publish Fog Analytics Result   #####################")
            print("##########################################################################################")
            Publish().publish(message=json.dumps(result), type="result")

