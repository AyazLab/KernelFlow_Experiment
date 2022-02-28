import os
# path to kernel socket module
cwd = os.getcwd()
os.chdir("..")
kernel_socket_path = os.path.join(os.getcwd(), "main", "kernel_socket")
os.chdir(cwd)

import sys
sys.path.insert(0, kernel_socket_path)

from kernel_socket import Marker

marker = Marker()
print(marker.IP)
print(marker.PORT)
marker.send_marker("experiment_start", log_file=False)