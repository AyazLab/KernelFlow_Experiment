#! C:\Users\zackg\AppData\Local\Programs\Python\Python39

#import socket
#from time import time
#import json

#id_val = 1
#timestamp = time()
#data_to_send = {
#    "id": id_val,
#    "timestamp": int(timestamp * 1e9),
#    "event": "start_experiment",
#    "value": "5",
#}
#event = json.dumps(data_to_send).encode("utf-8")
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.sendto(event, ("239.128.35.86", 7891))

#print("done")

import os
# path to kernel socket module
cwd = os.getcwd()
os.chdir("..")
kernel_socket_path = r"C:\Users\zackg\OneDrive\Ayaz Lab\KernelFlow_PsychoPy\main\kernel_socket"
os.chdir(cwd)
import sys
sys.path.insert(0, kernel_socket_path)
from kernel_socket import Marker
marker = Marker()

marker.send_marker("experiment_start")

print("done!")