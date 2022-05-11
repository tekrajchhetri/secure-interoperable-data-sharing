# -*- coding: utf-8 -*-
# @Time    : 08.05.22 11:22
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : Subscribe.py
# @Software: PyCharm
from connection_manager import ConnectionManager
from Pipeline import Pipeline
class Subscribe(ConnectionManager):
    def callback(self, ch, method, properties, body):
        pipeline = Pipeline()
        pipeline.init_pipeline(body)

    def subscribe(self):
        connection = self.rabbit_connection()
        channel = connection.channel()
        channel.basic_consume(
            queue=self.get_rabbit_config_details()["queuename"],
            on_message_callback=self.callback,
            auto_ack=True)
        channel.start_consuming()

if __name__ == '__main__':
    s = Subscribe()
    s.subscribe()