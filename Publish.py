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
        sensorobservationvalue = random.randint(10,100)
        timeStamp = datetime.now()
        sensorname = "DTH11"
        formattedTimeStampObservation = timeStamp.strftime("%Y%m%d%M%S%f")
        formattedTimeStampDT = timeStamp.strftime("%Y-%m-%dT%H:%M:%S:%f")
        data = {'observedproperty': 'STI_W201_humidity',
                'observationsensorid': sensorname,
                'observationresult': sensorobservationvalue,
                'resultobservationtime': f"{formattedTimeStampDT}",
                'observationid': f'{sensorname}_{formattedTimeStampObservation}',
                'hashvalue': self.generate_hash(formattedTimeStampObservation, sensorobservationvalue)
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
