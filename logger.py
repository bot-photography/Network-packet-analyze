import csv
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

LOG_TEXT_FILE = "packet_log.txt"
LOG_CSV_FILE = "packet_log.csv"

def log_packet_text(packet_info):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    entry = f"{timestamp} {packet_info}\n"
    with open(LOG_TEXT_FILE, "a") as f:
        f.write(entry)

def log_packet_csv(packet):
    from scapy.layers.inet import IP, TCP, UDP, ICMP

    if IP not in packet:
        return

    proto = "OTHER"
    if packet.haslayer(TCP):
        proto = "TCP"
    elif packet.haslayer(UDP):
        proto = "UDP"
    elif packet.haslayer(ICMP):
        proto = "ICMP"

    row = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Source IP": packet[IP].src,
        "Destination IP": packet[IP].dst,
        "Protocol": proto
    }

    file_exists = os.path.isfile(LOG_CSV_FILE)
    with open(LOG_CSV_FILE, "a", newline="") as csvfile:
        fieldnames = ["Timestamp", "Source IP", "Destination IP", "Protocol"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def info(message):
    print(f"{Fore.GREEN}[INFO] {Style.RESET_ALL}{message}")

def warning(message):
    print(f"{Fore.YELLOW}[WARNING] {Style.RESET_ALL}{message}")

def error(message):
    print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}{message}")

def packet_log(packet):
    from scapy.layers.inet import IP
    if IP in packet:
        summary = f"{packet[IP].src} ->  {packet[IP].dst} {packet.summary()}"

def log_packet(packet):
    """
    Logs packet to both text and CSV logs.
    """
    summary = packet.summary()
    log_packet_text(summary)
    log_packet_csv(packet)
