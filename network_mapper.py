import socket
import ipaddress
import re
import concurrent.futures

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

open_ports = []
closed_ports = []

def validate_ip_address(ip_address_str):
    try:
        ip_address_obj = ipaddress.ip_address(ip_address_str)
        return ip_address_obj
    except ValueError:
        return None

def get_protocol(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return "tcp"
    except (socket.error, socket.timeout):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)
                s.connect((ip, port))
                return "udp"
        except (socket.error, socket.timeout):
            return "unknown"

def check_port(ip, port):
    protocol = get_protocol(ip, port)
    
    if protocol == "tcp":
        open_ports.append((port, "tcp"))
        print(f"Port {port}/tcp is open on {ip}.")
    elif protocol == "udp":
        open_ports.append((port, "udp"))
        print(f"Port {port}/udp is open on {ip}.")
    else:
        closed_ports.append((port, "unknown"))
        print(f"Port {port} is closed on {ip}.")

def scan_ports(ip, port_min, port_max):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_port, ip, port) for port in range(port_min, port_max + 1)]

    # Wait for all threads to finish
    concurrent.futures.wait(futures)

if __name__ == "__main__":
    while True:
        ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
        ip_address_obj = validate_ip_address(ip_add_entered)
        
        if ip_address_obj:
            print("You entered a valid IP address.")
            break
        else:
            print("Invalid IP address. Please enter a valid IP address.")

    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (e.g., 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))

        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
        else:
            print("Invalid port range. Please enter a valid range.")

    scan_ports(ip_add_entered, port_min, port_max)

    print("\nScan complete.")
    if open_ports:
        print(f"Open ports on {ip_add_entered}: {open_ports}")
    else:
        print(f"No open ports found on {ip_add_entered}.")
