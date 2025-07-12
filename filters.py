from scapy.layers.inet import IP, TCP, UDP, ICMP

# User-defined filters
protocol_filter = None
ip_filter = None

def set_protocol_filter(protocol):
    global protocol_filter
    protocol_filter = protocol.upper()

def set_ip_filter(ip):
    global ip_filter
    ip_filter = ip

def match_filters(packet):
    if IP not in packet:
        return False

    if protocol_filter:
        if protocol_filter == "TCP" and not packet.haslayer(TCP):
            return False
        elif protocol_filter == "UDP" and not packet.haslayer(UDP):
            return False
        elif protocol_filter == "ICMP" and not packet.haslayer(ICMP):
            return False

    if ip_filter:
        src = packet[IP].src
        dst = packet[IP].dst
        if ip_filter != src and ip_filter != dst:
            return False

    return True
