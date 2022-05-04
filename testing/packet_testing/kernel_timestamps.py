import socket
import os
import json
import time

def return_byte_string():
    return b'\x0a'

socket_config_path = os.path.join(os.getcwd(), "socket_config.json")

socket_config = open(socket_config_path)
socket_data = json.load(socket_config)
socket_config.close()

kernel_IP = socket_data["kernel_IP"]
kernel_PORT = socket_data["kernel_PORT"]
psychopy_IP = socket_data["psychopy_IP"]
psychopy_PORT = socket_data["psychopy_PORT"]

print("Kernel PC IP:\t", kernel_IP)
print("Kernel PC PORT:\t", kernel_PORT)
print("PsychoPy PC IP:\t", psychopy_IP)
print("PsychoPy PC PORT:\t", psychopy_PORT, "\n")

opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket_receive.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
udp_socket_receive.bind(("", kernel_PORT))

print("Waiting to recieve...\n")
while True:
    data_bytes, addr = udp_socket_receive.recvfrom(1024)
    if data_bytes:
        recieved_timestamp = time.time_ns()
        sent_timestamp = time.time_ns()
        opened_socket.sendto(f"{recieved_timestamp},{sent_timestamp}".encode("utf-8"), (psychopy_IP, psychopy_PORT))