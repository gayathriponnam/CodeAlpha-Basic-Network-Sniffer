from scapy.all import sniff
from scapy.layers.inet import IP
print("Starting Network Sniffer...")
def show(packet):
    if packet.haslayer(IP):
        print("\nPacket Captured")
        print("Source IP :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        if packet[IP].proto == 6:
            print("Protocol : TCP")
        elif packet[IP].proto == 17:
            print("Protocol : UDP")
        else:
            print("Protocol :", packet[IP].proto)
sniff(prn=show, count=10)
