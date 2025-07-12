import os
from colorama import Fore, Style, init
from packet_sniffer import start_sniffing
from filters import set_protocol_filter, set_ip_filter
from data_viewer import view_logged_data
from plot_graph import plot_protocol_summary
from test_packets import generate_test_packets

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print(Fore.CYAN + "="*50)
    print(Fore.YELLOW + "   NETWORK PACKET ANALYZER".center(50))
    print(Fore.CYAN + "="*50)

def display_menu():
    print(Fore.GREEN + "\nOptions:")
    print("1. Start Packet Sniffing")
    print("2. Apply Protocol Filter")
    print("3. Apply IP Filter")
    print("4. View Logged Packets")
    print("5. Plot Protocol Summary")
    print("6. Generate Test Packets")
    print("7. Exit")

def main():
    while True:
        clear_screen()
        display_banner()
        display_menu()

        choice = input(Fore.BLUE + "\nEnter your choice (1-7): ")

        if choice == '1':
            print(Fore.MAGENTA + "\nSniffing packets...\n(Press Ctrl+C to stop)\n")
            try:
                start_sniffing()
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nStopped sniffing.")
            input(Fore.YELLOW + "\nPress Enter to return to menu...")

        elif choice == '2':
            protocol = input(Fore.CYAN + "Enter protocol to filter (TCP/UDP/ICMP): ").strip().upper()
            if protocol in ["TCP", "UDP", "ICMP"]:
                set_protocol_filter(protocol)
                print(Fore.GREEN + f"Protocol filter set to: {protocol}")
            else:
                print(Fore.RED + "Invalid protocol!")
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            ip = input(Fore.CYAN + "Enter IP address to filter (e.g., 192.168.1.1): ").strip()
            set_ip_filter(ip)
            print(Fore.GREEN + f"IP filter set to: {ip}")
            input("\nPress Enter to return to menu...")

        elif choice == '4':
            view_logged_data()
            input("\nPress Enter to return to menu...")

        elif choice == '5':
            plot_protocol_summary()
            input("\nPress Enter to return to menu...")

        elif choice == '6':
            print(Fore.MAGENTA + "Generating test packets...")
            generate_test_packets()
            input("\nPress Enter to return to menu...")

        elif choice == '7':
            print(Fore.GREEN + "\nExiting... Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
