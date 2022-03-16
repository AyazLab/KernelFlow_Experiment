#! C:\Users\zackg\AppData\Local\Programs\Python\Python39

import socket
from time import time
import json
id=1
timestamp = time()
data_to_send = {
    "id": id,
    "timestamp": int(timestamp * 1e9),
    "event": "trial_start",
    "value": "5",
}
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))