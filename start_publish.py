# -*- coding: utf-8 -*-
# @Time    : 12.05.22 13:26
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : start_publish.py
# @Software: PyCharm

from sensor.sensor import Sensor

from publisher.Publish import Publish
if __name__ == '__main__':
    s = Sensor()
    s.read_sensor_data()
    # p = Publish()
    # msg = p.format_data(55)
    # print(msg)
    # p.publish(msg, "data")

