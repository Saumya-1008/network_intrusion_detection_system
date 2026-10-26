
from scapy.all import sniff

def process(packet):
    print(packet.summary())

def start_sniffing():
    print("🚀 Starting packet capture...")
    sniff(prn=process, count=10)