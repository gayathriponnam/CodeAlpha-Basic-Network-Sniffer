# Basic Network Sniffer

## Description
The Basic Network Sniffer is a cybersecurity project developed using Python and the Scapy library. This tool captures live network packets and analyzes important information such as source IP address, destination IP address, and communication protocols. The project helps in understanding how data travels across networks and how packet monitoring is used in cybersecurity.

---

## Features
- Captures live network traffic packets
- Displays source IP addresses
- Displays destination IP addresses
- Identifies protocols such as:
  - TCP
  - UDP
  - ICMP
- Simple and efficient packet analysis

---

## Technologies Used
- Python
- Scapy Library

---

## How to Run the Project

### Step 1
Install Scapy using the following command:

pip install scapy
## Run the Python program:

python sniffer.py
## Step 3

The program will start capturing packets and display network information in the terminal.

## Sample Output
--- Packet Captured ---
Source IP: 104.18.39.21
Destination IP: 10.149.109.43
Protocol: TCP

