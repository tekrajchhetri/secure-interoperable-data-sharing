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
class Pipeline:

    def init_pipeline(self, data):
        data = json.loads(data)
        if(ValidationEngine().validate(data)):
            transformed_data = DataTransformationEngine().transform(data=data)
            status = DataMigration().migrate_to_gdb(transformed_data)
            print(data)
            return status


        # call legal engine
        # perform transformation
        # perform validation
        # perform analytics
        # migrate


