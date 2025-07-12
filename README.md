Network Packet Analyzer
A command-line Python tool for capturing, analyzing, filtering, and visualizing network traffic. Built with modular architecture for educational and cybersecurity research purposes.
📦 Features
- 🎯 Packet Sniffing – Monitor live network traffic using scapy
- 🧪 Apply Filters – Filter traffic by protocol or IP address
- 📄 View Data – Inspect logged packet data
- 📊 Protocol Visualization – Plot traffic distribution by protocol
- 🧬 Test Packet Generation – Inject synthetic packets for testing

🚀 Getting Started
Prerequisites
- Python 3.8+
- Administrator/root access (for sniffing packets)
- Required Python packages:
pip install scapy matplotlib colorama


Installation
Clone the repository:
git clone https://github.com/yourusername/network-packet-analyzer.git
cd network-packet-analyzer



🎮 How to Use
Run the main interface:
python main.py


You'll see a menu with the following options:
- Start Packet Sniffing – Begins live monitoring of packets
- Apply Protocol Filter – Filter by TCP, UDP, or ICMP
- Apply IP Filter – Narrow focus to specific IP traffic
- View Logged Packets – Display captured packet data
- Plot Protocol Summary – View distribution graph
- Generate Test Packets – Send synthetic packets for analysis
- Exit – Close the analyzer

🧠 Project Structure
| Module | Description | 
| main.py | Command-line interface and main loop | 
| packet_sniffer.py | Sniffs and logs live packets | 
| filters.py | Apply protocol/IP filters | 
| data_viewer.py | View captured data | 
| plot_graph.py | Protocol summary graph | 
| test_packets.py | Generates mock packets | 



📌 Notes
- Running sniffing functions may require administrative privileges.
- Packet generation uses scapy, and may be blocked by firewall settings.

🤝 Contributing
Open to suggestions, enhancements, and new modules! Feel free to fork, tweak, and pull.

📜 License
This project is licensed under the MIT License.

