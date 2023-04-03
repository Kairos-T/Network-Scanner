import socket
import subprocess
import sys

target = input("Enter the IP  address to scan: ")

try:
    socket.inet_aton(target)
except socket.error:
    print("Invalid IP address")
    sys.exit()

port_range = range(1, 100)

def scan(port): #TCP socket creation

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.5)

    try:
        s.connect((target, port))
        return True
    except:
        return False
    
for port in port_range:
    if scan(port):
        print(f"Port {port} is open")