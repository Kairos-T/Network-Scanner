import socket
import sys
import logging
import pyfiglet
from port_protocols import PORT_PROTOCOLS

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class InvalidIPAddressError(Exception):
    """
    Exception raised when an invalid IPv4 address is entered.
    """
    pass

class InvalidPortRangeError(Exception):
    """
    Exception raised when an invalid port range is entered.
    """
    pass

def is_valid_ip(ip):
    """
    Checks if a given string is a valid IPv4 address.

    Args:
        ip (str): The string to check.

    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    """
    
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_port(ip, port):
    """
    Scans a given port on a given IP address to check if it's open.

    Args:
        ip (str): The IP address to scan.
        port (int): The port number to scan.

    Returns:
        bool: True if the port is open, False otherwise.
    """
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except socket.timeout:
        return False
    except ConnectionRefusedError:
        return False

def main():
    """
    Runs the port scanner program.

    Prompts the user to enter an IPv4 address and a port range to scan.
    Scans the specified ports on the specified IP address and prints the open ports.

    Raises:
        InvalidIPAddressError: If the entered IP address is invalid.
        InvalidPortRangeError: If the entered port range is invalid.
    """
    
    title = pyfiglet.figlet_format("PORT SCANNER")
    print(title)
    
    while True:
        try:
            target = input("Enter the IPv4 address to scan (or 'exit' to quit): ")
            if target.lower() == 'exit':
                sys.exit()

            if not is_valid_ip(target):
                raise InvalidIPAddressError("Invalid IP address format. Please enter a valid IPv4 address.")

            start_port = int(input("Enter the starting port (Min: 1): "))
            end_port = int(input("Enter the ending port (Max: 65535): "))
            
            if start_port < 1 or end_port < start_port or end_port > 65535:
                raise InvalidPortRangeError("Invalid port range. Please enter port numbers between 1 and 65535.")
        except ValueError:
            logger.error("Invalid input. Please enter valid values.")
            continue
        except (InvalidIPAddressError, InvalidPortRangeError) as e:
            logger.error(str(e))
            continue

        open_ports = []

        print(f"Scanning ports from {start_port} to {end_port} on {target}...")

        for port in range(start_port, end_port + 1):
            if scan_port(target, port):
                open_ports.append(port)

        if open_ports:
            print("\nOpen ports:")
            for port in open_ports:
                protocol = PORT_PROTOCOLS.get(port, "Unknown")
                print(f"Port {port} is open (Protocol: {protocol})")
            print()
        else:
            print("No open ports found in the specified range.")

if __name__ == "__main__":
    main()
