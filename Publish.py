# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : Publish.py
# @Software: PyCharm
from connection_manager import ConnectionManager
import hashlib
from datetime import datetime
import json
import random
class Publish(ConnectionManager):

    def generate_hash(self, noise_timestamp, value):
        return hashlib.sha256(bytes(str(int(noise_timestamp) + value), 'utf-8')).hexdigest()

    def generate_data(self):
        sensorobservationvalue = random.randint(50,120)
        timestampval = datetime.now().strftime("%Y%m%d%M%S%f")
        data = {'observedproperty': 'STI_W201_temperature',
                'observationsensorid': 'DS18B20',
                'observationresult': sensorobservationvalue,
                'resultobservationtime': "2022-05-07",
                'observationid': f'DS18B20_{timestampval}',
                'hashvalue': self.generate_hash(timestampval, sensorobservationvalue)
                }
        return json.dumps(data)

    def publish(self, message):
        connection = self.rabbit_connection()
        channel = connection.channel()
        channel.basic_publish(exchange=self.get_rabbit_config_details()["exchange"],
                              routing_key=self.get_rabbit_config_details()["topic"],
                              body=message)
        connection.close()


if __name__ == '__main__':
    p = Publish()
    message = p.generate_data()
    p.publish(message)
        