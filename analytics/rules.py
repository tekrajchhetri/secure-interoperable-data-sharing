# -*- coding: utf-8 -*-
# @Time    : 12.05.22 17:44
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : rules.py
# @Software: PyCharm

class Rules:

    def get_swrl_rules(self):
        swrl_rules = {
           "temperature": """Observation(?observation),  
                    hasSimpleResult(?observation, ?result),
                    greaterThanOrEqual(?result, 75.0),
                    -> TemperatureAlert(?observation)""",

            "humidity": """Observation(?observation),  
                    hasSimpleResult(?observation, ?result),
                    greaterThanOrEqual(?result, 65.0),
                    -> HumidityAlert(?observation)""",

        }

        return swrl_rules
