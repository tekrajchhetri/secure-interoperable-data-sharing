# -*- coding: utf-8 -*-
# @Time    : 12.05.22 08:31
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : sensor.py
# @Software: PyCharm
import Adafruit_DHT
import yaml
from yaml.loader import SafeLoader
import sys
from data_migrator.Publish import Publish

class Sensor:
    def read_yml(self, filename):
        # Open the file and load the file
        try:
            with open(filename) as f:
                data = yaml.load(f, Loader=SafeLoader)
            return data
        except FileNotFoundError as e:
            sys.stderr.write("File not found")


    def read_sensor_data(self, mode):
        publishmsg = Publish()
        sensor_config = self.read_yml("sensor/sensor_config.yml")
        if mode=="edge":
            humidity, temperature = Adafruit_DHT.read_retry(eval(sensor_config["sensor"][0]["name"][0]),
                                                            sensor_config["sensor"][1]["gpio_pin"][0])
            message_temp = publishmsg.format_data(temperature)
            message_humidity = publishmsg.format_data(humidity, "humidity")
            # if we want to run on the edge device, there's no need to publish data to mesaging server
            # we can directly performing all the tasks and send the Kg to GraphDB
            return {"temperature": message_temp, "humidity":message_humidity}
        else:
            while True:
                humidity, temperature = Adafruit_DHT.read_retry(eval(sensor_config["sensor"][0]["name"][0]),
                            sensor_config["sensor"][1]["gpio_pin"][0])
                message_temp = publishmsg.format_data(temperature)
                message_humidity = publishmsg.format_data(humidity, "humidity")
                sys.stdout.write("Sending activitySensor data to Messaging Server")
                publishmsg.publish(message_temp, "data")
                publishmsg.publish(message_humidity, "data")
                sys.stdout.write("Send completed")