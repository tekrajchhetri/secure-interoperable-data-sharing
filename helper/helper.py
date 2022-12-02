# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : helper.py
# @Software: PyCharm
import yaml
from yaml.loader import SafeLoader
import  sys


class Helpers:

    def read_yml(self, filename):
        # Open the file and load the file
        try:
            with open(filename) as f:
                data = yaml.load(f, Loader=SafeLoader)
            return data
        except FileNotFoundError as e:
            sys.stderr.write("File not found")

    def get_rabbit_config_details(self):
        details = self.read_yml("core/config.yml")
        return {"username":details["rabbitdetails"][0]["username"][0],
                "password":details["rabbitdetails"][1]["password"][0],
                "hostname": details["rabbitdetails"][2]["host"][0],
                "data_publish_topic": details["rabbitdetails"][3]["data_publish_topic"][0],
                "port": details["rabbitdetails"][4]["port"][0],
                "data_publish_exchange": details["rabbitdetails"][5]["data_publish_exchange"][0],
                "queuename": details["rabbitdetails"][6]["queuename"][0],
                "result_publish_topic": details["rabbitdetails"][7]["result_publish_topic"][0],
                "result_publish_exchange": details["rabbitdetails"][8]["result_publish_exchange"][0],
                "result_queue": details["rabbitdetails"][9]["result_queue"][0]

                }

    def edge_intelligence_mode(self):
        details = self.read_yml("core/config.yml")
        return {"intelligence_mode":details["edgeintelligencemode"][0]["mode"][0] }

    def get_gdb_config_details(self):
        details = self.read_yml("core/config.yml")
        return {"username":details["graphdbdetails"][0]["username"][0],
                "password":details["graphdbdetails"][1]["password"][0],
                "hostname": details["graphdbdetails"][2]["host"][0],
                "repository": details["graphdbdetails"][3]["repository"][0]
                }

    def get_trustability(self):
        details = self.read_yml("core/config.yml")
        return {"sensor_manufacturers":details["trustability"][0]["sensor_manufacturers"][0],
                "deployed_location":details["trustability"][1]["deployed_location"][0],
                "deployed_by": details["trustability"][2]["deployed_by"][0],
                }



if __name__ == '__main__':
    "tests"
    h = Helpers()
    print(h.get_trustability())
