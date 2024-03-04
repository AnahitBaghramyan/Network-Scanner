# Port Scanner Readme

## Description

This Python script is a simple port scanner that allows users to scan a specified range of ports on a given IP address. The scanner supports both TCP and UDP protocols and utilizes multithreading to improve scanning efficiency.

## Features

- **IP Address Validation:** Ensures that the entered IP address is valid before initiating the scan.
- **Port Range Specification:** Allows users to define a custom range of ports to scan.
- **TCP and UDP Support:** Determines whether a port is open for both TCP and UDP protocols.
- **Multithreading:** Utilizes concurrent threads to speed up the scanning process.

## Usage

1. Run the script and follow the prompts.
2. Enter a valid IP address when prompted.
3. Specify the range of ports to scan in the format `<int>-<int>` (e.g., 60-120).
4. The script will then scan the specified ports and display the results.

## Requirements

- Python 3.x

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using the command: `python port_scanner.py`

## Example

```bash
Please enter the IP address that you want to scan: 192.168.1.1
You entered a valid IP address.

Please enter the range of ports you want to scan in format: <int>-<int> (e.g., 60-120)
Enter port range: 80-100
Port 80/tcp is open on 192.168.1.1.
Port 85/tcp is open on 192.168.1.1.
Port 90/tcp is closed on 192.168.1.1.
...
Scan complete.
Open ports on 192.168.1.1: [(80, 'tcp'), (85, 'tcp')]
```
