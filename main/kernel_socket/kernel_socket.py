import socket
import csv
import os
import json
import pandas as pd
import sys
from psychopy import logging
from time import time

class Marker():
    def __init__(self):
        self.opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_config_path = self.get_socket_path()
        self.marker_dict_path = self.get_marker_dict_path()
        self.marker_dict = self.make_marker_dict(self.marker_dict_path)
        self.kernel_IP, self.kernel_PORT = self.get_socket_info(self.socket_config_path)

    def get_socket_path(self): 
        cwd = os.getcwd()
        temp_path = cwd.split("\\KernelFlow_PsychoPy")[0]
        socket_config_path = os.path.join(temp_path, "KernelFlow_PsychoPy", "main", "kernel_socket", "socket_config.json")

        return socket_config_path

    def get_socket_info(self, socket_config_path):
        socket_config = open(socket_config_path)
        socket_data = json.load(socket_config)
        socket_config.close()

        kernel_IP = socket_data["kernel_IP"]
        kernel_PORT = socket_data["kernel_PORT"]

        return kernel_IP, kernel_PORT

    def get_marker_dict_path(self):
        cwd = os.getcwd()
        temp_path = cwd.split("\\KernelFlow_PsychoPy")[0]
        marker_dict_path = os.path.join(temp_path, "KernelFlow_PsychoPy", "main", "marker_dict.csv")

        return marker_dict_path

    def make_marker_dict(self, marker_dict_path):
        df = pd.read_csv(self.marker_dict_path)
        marker_vals =df["marker_val"]
        marker_strs = df["marker_str"]

        marker_dict = {}
        for marker_val, marker_str in zip(marker_vals, marker_strs):
            marker_dict[str(marker_val)] = marker_str

        return marker_dict

    def send_marker(self, marker_val, timestamp):
        if str(marker_val)[1] == "1":
            marker_str = "start_experiment"
        elif str(marker_val)[1] == "2":
            marker_str = "end_experiment"
        else:
            marker_str = "Marker ERROR"
        
        data_to_send = {
            "id": 1,
            "timestamp": timestamp,
            "event": marker_str,
            "value": str(marker_val)
        }
        
        event = json.dumps(data_to_send).encode("utf-8")
        self.opened_socket.sendto(event, (self.kernel_IP, self.kernel_PORT))

        exp_marker_str = self.marker_dict[str(marker_val)]

        logging.log(msg=f"UDP Sent: marker_value={marker_val}, marker_string={exp_marker_str}, timestamp={timestamp}", level=logging.EXP)