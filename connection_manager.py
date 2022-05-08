# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:33
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : connection_manager.py
# @Software: PyCharm

import pika
from helper import Helpers

class ConnectionManager(Helpers):
    def create_rabbit_connection(self):
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