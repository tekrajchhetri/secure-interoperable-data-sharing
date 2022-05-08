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
    def __init__(self):
        sys.stdout.write("init helpers")

    def read_yml(self, filename):
        # Open the file and load the file
        try:
            with open(filename) as f:
                data = yaml.load(f, Loader=SafeLoader)
            return data
        except FileNotFoundError as e:
            sys.stderr.write("File not found")

    def get_rabbit_config_details(self):
        details = self.read_yml("config.yml")
        return {"username":details["rabbitdetails"][0]["username"][0],
                "password":details["rabbitdetails"][1]["password"][0],
                "hostname": details["rabbitdetails"][2]["host"][0],
                "topic": details["rabbitdetails"][3]["topic"][0],
                }
