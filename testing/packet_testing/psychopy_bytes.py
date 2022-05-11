import socket
import os
import json
import time
import ctypes
import statistics
import pandas as pd

def return_byte_string():
    return b'\x0a'

def micros():
    "return a timestamp in microseconds (us)"
    tics = ctypes.c_int64()
    freq = ctypes.c_int64()

    #get ticks on the internal ~2MHz QPC clock
    ctypes.windll.Kernel32.QueryPerformanceCounter(ctypes.byref(tics)) 
    #get the actual freq. of the internal ~2MHz QPC clock
    ctypes.windll.Kernel32.QueryPerformanceFrequency(ctypes.byref(freq))  
    
    t_us = tics.value*1e6/freq.value

    return t_us

socket_config_path = os.path.join(os.getcwd(), "kernel_socket", "socket_config.json")

socket_config = open(socket_config_path)
socket_data = json.load(socket_config)
socket_config.close()

kernel_IP = socket_data["kernel_IP"]
kernel_PORT = socket_data["kernel_PORT"]
psychopy_IP = socket_data["psychopy_IP"]
psychopy_PORT = socket_data["psychopy_PORT"]

print("Kernel PC IP: ", kernel_IP)
print("Kernel PC PORT: ", kernel_PORT)
print("PsychoPy PC IP: ", psychopy_IP)
print("PsychoPy PC PORT: ", psychopy_PORT, "\n")

opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket_receive.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
udp_socket_receive.bind(("", psychopy_PORT)) 

# One byte testing

num_packets = 0
psychopy_sent_micros_list = []
psychopy_recv_micros_list = []
t_start = micros()
while num_packets < 10000:
    opened_socket.sendto(return_byte_string(), (kernel_IP, kernel_PORT))
    psychopy_sent_micros_list.append(micros())
    data_bytes = udp_socket_receive.recvfrom(1024)
    if data_bytes:
        psychopy_recv_micros_list.append(micros())
        num_packets += 1

bytes_df = pd.DataFrame(list(zip(psychopy_sent_micros_list, psychopy_recv_micros_list)), columns=["Sent (us)", "Received (us)"])
bytes_df.loc[:, "Two-way time (us)"] = bytes_df.loc[:, "Received (us)"].subtract(bytes_df.loc[:, "Sent (us)"])
bytes_df.loc[:, "One-way time (us)"] = bytes_df.loc[:, "Two-way time (us)"].divide(2)

print("Num packets: ", len(bytes_df))
print("One-way Mean (ms): ", round(bytes_df["One-way time (us)"].mean()/1000, 4))
print("One-way STD (ms): ", round(bytes_df["One-way time (us)"].std()/1000, 4))

filename = "packet_bytes_df.xlsx"
filepath = os.path.join(os.getcwd(), filename)

writer = pd.ExcelWriter(filepath)
bytes_df.to_excel(writer)
writer.save()