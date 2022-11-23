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
from legal.legal_engine import LegalEngine
from helper.helper import Helpers
class Pipeline:


    def validate_transform_migrate(self, data):
        data = json.loads(data)
        if LegalEngine().hasConsent(data=data):
            validation_result = ValidationEngine().validate(data)
            if(validation_result["status"]):
                transformed_data = DataTransformationEngine().transform(rdf_data=
                                                                        ValidationEngine().turtle_str_to_rdf_graph(
                                                                            validation_result["rdf_turtle_data"]
                                                                        )
                                                                        )
                status = DataMigration().migrate_to_gdb(transformed_data)
                print(status)
                return status 
        else:
            print({"message":"Unable to process due to a lack of consent for the requested operation."})

    def validate_apply_intelligence(self, data):
        data = json.loads(data)
        if LegalEngine().hasConsent(data=data):
            mode = Helpers().edge_intelligence_mode()["intelligence_mode"]
            validation_result = ValidationEngine().validate(data)
            if (validation_result["status"]):
                if mode == "edge":
                    res = EdgeIntelligence().start_edge_intelligence(data, mode)
                    print(res)
                else:
                    EdgeIntelligence().start_edge_intelligence(data, mode)
        else:
            print({"message":"Unable to process due to a lack of consent for the requested operation."})


