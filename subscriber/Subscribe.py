# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:22
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : Subscribe.py
# @Software: PyCharm
from core.connection_manager import ConnectionManager
from pipeline.Pipeline import Pipeline
class Subscribe(ConnectionManager):
    def callback(self, ch, method, properties, body):
        pipeline = Pipeline()
        r = pipeline.validate_transform_migrate(body)
        pipeline.validate_apply_intelligence(body)

    def fog_result_callback(self, ch, method, properties, body):
        """This is where you'd implement call to control action based on fog results
        """
        print("##########################################################################################")
        print(f"######################    Fog  Result  callback for future         #####################")
        print("##########################################################################################")
        print(body)

    def subscribe(self):
        connection = self.rabbit_connection()
        channel = connection.channel()
        channel.basic_consume(
            queue=self.get_rabbit_config_details()["queuename"],
            on_message_callback=self.callback,
            auto_ack=True)
        channel.start_consuming()

    def subscribe_fog_result(self):
        connection = self.rabbit_connection()
        channel = connection.channel()
        channel.basic_consume(
            queue=self.get_rabbit_config_details()["result_queue"],
            on_message_callback=self.fog_result_callback,
            auto_ack=True)
        channel.start_consuming()
