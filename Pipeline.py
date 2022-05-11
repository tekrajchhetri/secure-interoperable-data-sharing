# -*- coding: utf-8 -*-
# @Time    : 09.05.22 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : Pipeline.py
# @Software: PyCharm
from validation_engine import ValidationEngine
from data_migration import DataMigration
import json
class Pipeline:
    def __int__(self):
        self.ve = ValidationEngine()

    def init_pipeline(self, data):
        data = json.loads(data)
        print()
        print("From pipeline")
        print(data)

        print(ValidationEngine().data_quality_validation(data))
        # call legal engine
        # perform transformation
        # perform validation
        # perform analytics
        # migrate


