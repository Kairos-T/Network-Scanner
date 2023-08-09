import socket
import sys

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        s.close()  # Close the socket after successful connection
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def main():
    target = input("Enter the IP address to scan: ")

    if not is_valid_ip(target):
        print("Invalid IP address")
        sys.exit()

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
    except ValueError:
        print("Invalid port range")
        sys.exit()

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found in the specified range.")

if __name__ == "__main__":
    main()
