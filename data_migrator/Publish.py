# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : Publish.py
# @Software: PyCharm
from core.connection_manager import ConnectionManager
import hashlib
from datetime import datetime
import json
from data_transformation.data_transformation_engine import DataTransformationEngine
from smart_contract.transaction import Transaction
from legal.legal_engine import LegalEngine

class Publish(ConnectionManager):

    def generate_hash(self, noise_timestamp, value):
        return hashlib.sha256(bytes(str(int(noise_timestamp) + round(float(value), 3)), 'utf-8')).hexdigest()

    def format_data(self, sensorobservationvalue, type="temperature"):
        observed_property = f'STI_W201_{type}'
        timeStamp = datetime.now()
        sensorname = "DHT11"
        formattedTimeStampObservation = timeStamp.strftime("%Y%m%d%M%S")
        formattedTimeStampDT = timeStamp.strftime("%Y-%m-%dT%H:%M:%S")
        hashValue = self.generate_hash(formattedTimeStampObservation, sensorobservationvalue)
        blockchainHash = Transaction().create_transaction(hashValue)
        data = {'observedproperty': observed_property,
                'observationsensorid': sensorname,
                'observationresult': sensorobservationvalue,
                'resultobservationtime': f"{formattedTimeStampDT}",
                'observationid': f'{sensorname}_{formattedTimeStampObservation}',
                'blockchainhashvalue':blockchainHash
                }
        return json.dumps(DataTransformationEngine().generate_shacl_data_graph(data))

    def publish(self, message, type):
        connection = self.rabbit_connection()
        if type == "data":
            exchange_name = self.get_rabbit_config_details()["data_publish_exchange"]
            topic = self.get_rabbit_config_details()["data_publish_topic"]
        elif type == "result":
            print("##########################################################################################")
            print(f"######################   Publishing Fog Analytics Result            #####################")
            print("##########################################################################################")
            exchange_name = self.get_rabbit_config_details()["result_publish_exchange"]
            topic = self.get_rabbit_config_details()["result_publish_topic"]
        if LegalEngine().hasConsent(message):
            print("##########################################################################################")
            print(f"######################   Checking Consent                           #####################")
            print("##########################################################################################")
            channel = connection.channel()
            channel.basic_publish(exchange=exchange_name,
                                  routing_key=topic,
                                  body=message)
            connection.close()
        else:
            print("No consent")