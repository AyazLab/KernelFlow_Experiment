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
participant_ID_recieved = False
while not participant_ID_recieved:
    data_bytes, addr = udp_socket_receive.recvfrom(1024)
    if data_bytes:
        recieved_timestamp = str(time.time())
        recieved_data = data_bytes.decode("utf-8") 
        print("Recieved at:\t", recieved_timestamp)
        participant_ID_recieved = True
    else:
        pass

kernel_sent_timestamp = str(time.time())
udp_data = f"{recieved_timestamp},{kernel_sent_timestamp}".encode("utf-8")
opened_socket.sendto(udp_data, (psychopy_IP, psychopy_PORT))
print("Sent at:\t", kernel_sent_timestamp)

psychopy_sent_timestamp = recieved_data.split(",")[0]
participant_ID = recieved_data.split(",")[1]
filename = f"participant_{participant_ID}_" + "marker_log" + ".txt"   
filepath = os.path.join(os.getcwd(), "participants", filename)                        

print("\nMarker log filename:\t", filename, "\n")
udp_file = open(filepath, 'w')
udp_file.write("PsychoPy PC sent at\t" + psychopy_sent_timestamp + "\nKernel PC recieved at\t" + recieved_timestamp + "\n") 
udp_file.flush() 
udp_file.write("\nKernel PC sent at\t" + kernel_sent_timestamp) 
udp_file.flush() 
udp_file.close()
