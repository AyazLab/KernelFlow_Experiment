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

# Timestamp testing

psychopy_sent_timestamp_list = []
psychopy_recv_timestamp_list = []
psychopy_sent_micros_list = []
psychopy_recv_micros_list = []
raw_kernel_packets_list = []

num_packets = 0
while num_packets < 1000:
    sent_timestamp = time.time_ns()
    opened_socket.sendto(f"{sent_timestamp}".encode("utf-8"), (kernel_IP, kernel_PORT))
    psychopy_sent_micros_list.append(micros())
    data_bytes, addr = udp_socket_receive.recvfrom(1024)
    if data_bytes:
        psychopy_recv_timestamp_list.append(time.time_ns())
        psychopy_recv_micros_list.append(micros())
        raw_kernel_packets_list.append(data_bytes)
        num_packets += 1
    psychopy_sent_timestamp_list.append(sent_timestamp)

kernel_recv_timestamp_list = []
kernel_sent_timestamp_list = []

for kernel_packet in raw_kernel_packets_list:
    kernel_data = kernel_packet.decode("utf-8") 
    kernel_recv_timestamp_list.append(float(kernel_data.split(",")[0]))
    kernel_sent_timestamp_list.append(float(kernel_data.split(",")[1]))

bytes_timestamps_df = pd.DataFrame(list(zip(psychopy_sent_micros_list, psychopy_recv_micros_list)), columns=["Sent (us)", "Recieved (us)"])
bytes_timestamps_df.loc[:, "Two-way time (us)"] = bytes_timestamps_df.loc[:, "Recieved (us)"].subtract(bytes_timestamps_df.loc[:,"Sent (us)"])
bytes_timestamps_df.loc[:, "One-way time (us)"] = bytes_timestamps_df.loc[:, "Two-way time (us)"].divide(2)
bytes_timestamps_df["PsychoPy Sent (UTC)"] = psychopy_sent_timestamp_list
bytes_timestamps_df["PsychoPy Recv (UTC)"] = psychopy_recv_timestamp_list
bytes_timestamps_df["Kernel Sent (UTC)"] = kernel_sent_timestamp_list
bytes_timestamps_df["Kernel Recv (UTC)"] = kernel_recv_timestamp_list

print("Num packets: ", len(bytes_timestamps_df))
one_way_mean_us = bytes_timestamps_df["One-way time (us)"].mean()
print("One-way Mean (ms): ", round(one_way_mean_us/1000, 4))
one_way_std_us = bytes_timestamps_df["One-way time (us)"].std()
print("One-way Std (ms): ", round(one_way_std_us/1000, 4))

one_way_mean_s = one_way_mean_us * 1e6

# T2-(T1+t1)
bytes_timestamps_df["Clock delta (us)"] = bytes_timestamps_df.loc[:, "Kernel Recv (UTC)"].subtract(bytes_timestamps_df.loc[:, "PsychoPy Sent (UTC)"].add(one_way_mean_s))
bytes_timestamps_df["Clock delta (us)"] = bytes_timestamps_df.loc[:, "Clock delta (us)"].divide(1e6)

# If negative, Kernel clock is behind
# If positive, Kernel clock is ahead
clock_delta_mean = bytes_timestamps_df["Clock delta (us)"].mean()
print("Clock-delta Mean (ms): ", round(clock_delta_mean/1000, 4))
clock_delta_std = bytes_timestamps_df["Clock delta (us)"].std()
print("Clock-delta Std (ms): ", round(clock_delta_std/1000, 4))

filename = "packet_bytes_timestamps_df.xlsx"
filepath = os.path.join(os.getcwd(), filename)

writer = pd.ExcelWriter(filepath)
bytes_timestamps_df.to_excel(writer)
writer.save()