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
from  publisher.Publish import Publish

class Sensor:
    def read_yml(self, filename):
        # Open the file and load the file
        try:
            with open(filename) as f:
                data = yaml.load(f, Loader=SafeLoader)
            return data
        except FileNotFoundError as e:
            sys.stderr.write("File not found")


    def read_sensor_data(self):
        publishmsg = Publish()
        sensor_config = self.read_yml("sensor/sensor_config.yml")
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(eval(sensor_config["sensor"][0]["name"][0]),
                                                            sensor_config["sensor"][1]["gpio_pin"][0])
            print(f"Humidity = {humidity}%, Temperature={temperature} degree Celcius")
            message = publishmsg.format_data(temperature)
            publishmsg.publish(message)
            message = publishmsg.format_data(humidity,"humidity")
            publishmsg.publish(message)