# -*- coding: utf-8 -*-
# @Time    : 12.05.22 13:40
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : start_operations.py
# @Software: PyCharm

from sensor.sensor import Sensor
from helper.helper import Helpers
from pipeline.Pipeline import Pipeline
from subscriber.Subscribe import Subscribe
if __name__ == '__main__':
    s = Sensor()
    pipeline = Pipeline()
    mode = Helpers().edge_intelligence_mode()["intelligence_mode"]
    if mode == "edge":
        sensor_data = s.read_sensor_data(mode=mode)
        pipeline.validate_transform_migrate(sensor_data["humidity"])
        pipeline.validate_apply_intelligence(sensor_data["humidity"])
        pipeline.validate_transform_migrate(sensor_data["temperature"])
        pipeline.validate_apply_intelligence(sensor_data["temperature"])
    else:
        s = Subscribe()
        s.subscribe()
