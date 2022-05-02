import socket
import os
import json
import time

socket_config_path = os.path.join(os.getcwd(), "kernel_socket", "socket_config.json")

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
udp_socket_receive.bind(("", psychopy_PORT))

participant_ID = input("Enter participant ID: ")
participant_ID = f"{int(participant_ID):02d}"

filename = f"participant_{participant_ID}_" + "marker_log" + ".txt"   
filepath = os.path.join(os.path.dirname(os.getcwd()), "participants", f"participant_{participant_ID}", filename)                        

sent_timestamp = str(time.time())
udp_data = f"{sent_timestamp},{participant_ID}".encode("utf-8")
opened_socket.sendto(udp_data, (kernel_IP, kernel_PORT))
print("\nSent at:\t", sent_timestamp, "\n")

print("Waiting to recieve...\n")
response_recieved = False
while not response_recieved:
    data_bytes, addr = udp_socket_receive.recvfrom(1024)
    if data_bytes:
        recieved_timestamp = str(time.time())
        kernel_data = data_bytes.decode("utf-8") 
        kernel_recieved_timestamp = kernel_data.split(",")[0]
        kernel_sent_timestamp = kernel_data.split(",")[1]
        print("Recieved at:\t", recieved_timestamp)
        response_recieved = True
    else:
        pass

print("\nMarker log filename:\t", filename)
udp_file = open(filepath, 'w')
udp_file.write("PsychoPy PC sent at:\t" + sent_timestamp + "\nKernel PC recieved at:\t" + kernel_recieved_timestamp + "\n") 
udp_file.flush() 
udp_file.write("Kernel PC sent at:\t" + kernel_sent_timestamp + "\nPsychoPy PC recieved at:\t" + recieved_timestamp) 
udp_file.flush() 
udp_file.close()
