import socket
import csv
import os
import json
import pandas as pd
import sys
from psychopy import logging

class Marker():
    def __init__(self):
        self.opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_config_path = self.get_socket_path()
        self.marker_dict_path = self.get_marker_dict_path()
        self.marker_dict = self.make_marker_dict(self.marker_dict_path)
        self.IP, self.PORT = self.get_socket_info(self.socket_config_path)

    def get_socket_path(self): 
        #cwd = os.getcwd()
        #os.chdir("..")
        #socket_config_path = os.path.join(os.getcwd(), r"main\kernel_socket", "socket_config.json")
        #os.chdir(cwd)

        cwd = os.getcwd()
        temp_path = cwd.split("\\KernelFlow_PsychoPy")[0]
        socket_config_path = os.path.join(temp_path, "KernelFlow_PsychoPy", "main", "kernel_socket", "socket_config.json")
        print("socket path: ", socket_config_path)

        return socket_config_path

    def get_socket_info(self, socket_config_path):
        socket_config = open(socket_config_path)
        socket_data = json.load(socket_config)
        socket_config.close()

        IP = socket_data["IP"]
        PORT = socket_data["PORT"]

        return IP, PORT

    def get_marker_dict_path(self):
        #cwd = os.getcwd()
        #os.chdir("..")
        #marker_dict_path = os.path.join(os.getcwd(), "main", "marker_dict.csv")
        #os.chdir(cwd)

        cwd = os.getcwd()
        temp_path = cwd.split("\\KernelFlow_PsychoPy")[0]
        marker_dict_path = os.path.join(temp_path, "KernelFlow_PsychoPy", "main", "marker_dict.csv")
        print("marker path: ", marker_dict_path)

        return marker_dict_path

    def make_marker_dict(self, marker_dict_path):
        df = pd.read_csv(self.marker_dict_path)
        marker_strs = df["marker_str"]
        marker_vals =df["marker_val"]

        marker_dict = {}
        for marker_str, marker_val in zip(marker_strs, marker_vals):
            marker_dict[marker_str] = marker_val

        return marker_dict

    def send_marker(self, marker_str, log_file=True):
        marker_val = self.marker_dict[marker_str]
        byte_message = int(marker_val).to_bytes(1,'big')
        self.opened_socket.sendto(byte_message, (self.IP, self.PORT))
        if log_file == True:
            logging.log(msg=f"UDP Sent: marker_value={marker_val}, marker_string={marker_str}", level=logging.EXP)
        else:
            print(f"UDP Sent: marker value={marker_val}, marker string={marker_str}")