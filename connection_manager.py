# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:33
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : connection_manager.py
# @Software: PyCharm

import pika
from helper import Helpers
from SPARQLWrapper import SPARQLWrapper, BASIC

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


