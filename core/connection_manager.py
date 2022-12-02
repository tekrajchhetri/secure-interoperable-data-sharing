# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:33
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : connection_manager.py
# @Software: PyCharm

import json
import pika
from helper.helper import Helpers
from SPARQLWrapper import SPARQLWrapper, BASIC
import requests

class ConnectionManager(Helpers):
    def rabbit_connection(self):
        connection_details = self.get_rabbit_config_details()
        username = connection_details["username"]
        password = connection_details["password"]
        hostname = connection_details["hostname"]
        port = connection_details["port"]
        credentials = pika.PlainCredentials(username, password)
        connection_parameters = pika.ConnectionParameters(
            host=hostname,
            port=port,
            virtual_host="/",
            credentials=credentials
        )

        connection = pika.BlockingConnection(connection_parameters)
        return connection

    def graphdb_connection(self, type="get"):
        connection_details = self.get_gdb_config_details()
        username = connection_details["username"]
        password = connection_details["password"]
        if type=="get":
            hostname = f"{connection_details['hostname']}/{connection_details['repository']}"
        elif type=="post":
            hostname = f"{connection_details['hostname']}/{connection_details['repository']}/statements"
        sparql = SPARQLWrapper(hostname)
        sparql.setHTTPAuth(BASIC)
        sparql.setCredentials(username, password)
        return sparql

    def get_trustability_score(self):
        data = self.get_trustability()
        _URL = data["url"]

        payload = {
            "sensor_manufacturers": data["sensor_manufacturers"],
            "deployed_location": data["deployed_location"],
            "deployed_by": data["deployed_by"]
        }
        _r = requests.post(_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        return json.loads(_r.text)["trustability"]


if __name__ == '__main__':
    c = ConnectionManager()
    print(c.get_trustability_score())



