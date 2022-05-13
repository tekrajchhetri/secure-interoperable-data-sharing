# -*- coding: utf-8 -*-
# @Time    : 23.01.22 23:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_transformation_engine.py
# @Software: PyCharm
import sys
from rdflib import Graph
class DataTransformationEngine:
    def transform(self, rdf_data):
        transformed_data = ""
        for subject, predicate, obj in rdf_data:
            transformed_data = transformed_data + subject.n3() + " " + predicate.n3() + " " + obj.n3() + " . \n"

        return transformed_data