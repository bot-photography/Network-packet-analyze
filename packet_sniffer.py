from scapy.all import sniff
from scapy.layers.inet import TCP, UDP, ICMP, IP
from scapy.config import conf

from filters import match_filters
from logger import log_packet, packet_log

# Initialize protocol counters
packet_count = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "OTHER": 0,
    "TOTAL": 0
}

def process_packet(packet):
    if match_filters(packet):
        packet_log(packet)
        log_packet(packet)
        return

    # Log to text + console + CSV
    summary = packet.summary()
    log_packet(summary)       # log to packet_log.txt
    packet_log(packet)        # log to console + CSV

    # Count protocols
    packet_count["TOTAL"] += 1
    if packet.haslayer(TCP):
        packet_count["TCP"] += 1
    elif packet.haslayer(UDP):
        packet_count["UDP"] += 1
    elif packet.haslayer(ICMP):
        packet_count["ICMP"] += 1
    else:
        packet_count["OTHER"] += 1

    # Print summary every 10 packets
    if packet_count["TOTAL"] % 10 == 0:
        print("\n--- Protocol Summary ---")
        print(f"TCP:   {packet_count['TCP']}")
        print(f"UDP:   {packet_count['UDP']}")
        print(f"ICMP:  {packet_count['ICMP']}")
        print(f"Other: {packet_count['OTHER']}")
        print(f"Total: {packet_count['TOTAL']}")
        print("-------------------------\n")

def start_sniffing():
    sniff(prn=process_packet, store=False, iface=conf.iface, filter="ip")
