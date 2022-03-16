import socket
import time
import struct
import os

UDP_IP = '127.0.0.1'

UDP_PORT_Receive = 5501
UDP_PORT_Relay1 = 5504
UDP_PORT_Relay2 = 5508

udp_socket_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket_relay_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket_relay_1 =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket_receive.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
udp_socket_relay_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
udp_socket_relay_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
#udp_socket_relay_1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#udp_socket_relay_2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

udp_socket_receive.bind(("", UDP_PORT_Receive))
#udp_socket_relay_1.bind(("127.0.0.1", UDP_PORT_Relay1))

#udp_socket_relay_2.bind(("127.0.0.1", UDP_PORT_Relay2))

#mreq = struct.pack("=4sl", socket.inet_aton("127.0.0.1"), socket.INADDR_ANY)
#udp_socket_receive.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Hostname :  ",host_name)
print("DAQ IP : "+host_ip+"\n")

print("Listening  to port #i", UDP_PORT_Receive)
print("Relaying  to port #i", UDP_PORT_Relay1)
print("Relaying  to port #i", UDP_PORT_Relay2)

#tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#tcp_socket.bind((TCP_IP, TCP_PORT))
#tcp_socket.listen(100)
#conn, addr = tcp_socket.accept()

print("Address bound\n");

def relayMarker(msg):
    udp_socket_relay_1.sendto(msg,("127.0.0.1", UDP_PORT_Relay1));
    udp_socket_relay_2.sendto(msg,("127.0.0.1", UDP_PORT_Relay2));

relayMarker(b"1")

# ----- save file
output_dir = os.path.join(os.getcwd(), "udp_files")

if os.path.exists(output_dir):  # if dir exists
    pass
else:                           # if dir doesnt exist, create it
    os.mkdir(output_dir)

filename = "UDP-" + str(time.time()).replace(".", "") + ".txt"  # file name
filepath = os.path.join(output_dir, filename)                   # file path

udp_file = open(filepath, 'w')    

while True:
    dataBytes, addr = udp_socket_receive.recvfrom(1024)
    print("Recieved")
    data = dataBytes.decode("utf-8") 
    print(data + "\n")
    udp_file.write(data + "\n") 
    udp_file.flush() 
    
    relayMarker(dataBytes)
        