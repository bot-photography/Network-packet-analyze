from scapy.all import IP, TCP, UDP, ICMP
from logger import packet_log, log_packet_text, log_packet_csv

def generate_test_packets():
    print("\nSimulating test packets...\n")

    # Create a sample TCP packet
    tcp_packet = IP(src="192.168.1.2", dst="192.168.1.10") / TCP(sport=1234, dport=80)

    # Create a sample UDP packet
    udp_packet = IP(src="10.0.0.5", dst="10.0.0.10") / UDP(sport=5000, dport=53)

    # Create a sample ICMP packet
    icmp_packet = IP(src="8.8.8.8", dst="192.168.1.1") / ICMP()

    test_packets = [tcp_packet, udp_packet, icmp_packet]

    for pkt in test_packets:
        try:
            packet_log(pkt)                      # Print to console
            log_packet_text(pkt.summary())       # Save to text log
            log_packet_csv(pkt)                  # Save to CSV log
        except Exception as e:
            print(f"[ERROR] Failed to log test packet: {e}")

    print("\n✅ Test packets generated and logged successfully.")
