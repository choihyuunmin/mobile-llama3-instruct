from scapy.all import sniff, IP, TCP
import time
import threading

# Dictionary to track SYN packets {source IP: {"count": SYN packet count, "timestamp": first detected time}}
syn_tracker = {}
reset_interval = 3600  # 1 hour (3600 seconds)
alert_threshold = 5000  # SYN flood detection threshold

# Function to reset data every hour
def reset_tracker():
    global syn_tracker
    while True:
        time.sleep(reset_interval)
        print("\n[INFO] Resetting SYN tracker data...\n")
        syn_tracker.clear()

# Packet processing function
def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        if packet[TCP].flags & 2:  # Check SYN flag
            src_ip = packet[IP].src
            current_time = time.time()

            if src_ip not in syn_tracker:
                syn_tracker[src_ip] = {"count": 1, "timestamp": current_time}
            else:
                syn_tracker[src_ip]["count"] += 1

            count = syn_tracker[src_ip]["count"]

            if count > alert_threshold:
                print(f"[ALERT] Potential SYN Flood Attack Detected from {src_ip} - SYN Count: {count}")

# Start a background thread to reset data every hour
reset_thread = threading.Thread(target=reset_tracker, daemon=True)
reset_thread.start()

# Start packet sniffing (Change 'eth0' or 'wlan0' based on your network interface)
print("[INFO] Starting packet capture...")
sniff(filter="tcp", prn=packet_callback, store=False)