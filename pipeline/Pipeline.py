# -*- coding: utf-8 -*-
# @Time    : 09.05.22 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : Pipeline.py
# @Software: PyCharm
from validation.validation_engine import ValidationEngine
import json
from data_migrator.data_migration import DataMigration
from data_transformation.data_transformation_engine import DataTransformationEngine
from analytics.edge_intelligence import EdgeIntelligence
from helper.helper import Helpers
class Pipeline:

    def validate_transform_migrate(self, data):
        data = json.loads(data)
        if(ValidationEngine().validate(data)):
            transformed_data = DataTransformationEngine().transform(data=data)
            status = DataMigration().migrate_to_gdb(transformed_data)
            return status

    def validate_apply_intelligence(self, data):
        data = json.loads(data)
        mode = Helpers().edge_intelligence_mode()["intelligence_mode"]
        if (ValidationEngine().validate(data)):
            if mode=="edge":
                res =  EdgeIntelligence().start_edge_intelligence(data, mode)
                print(res)
            else:
                EdgeIntelligence().start_edge_intelligence(data, mode)

