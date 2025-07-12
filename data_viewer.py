import csv
from colorama import Fore, Style

CSV_FILE = "packet_log.csv"

def view_logged_data():
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            print(Fore.YELLOW + "\nLogged Packets:\n" + Fore.RESET)
            for i, row in enumerate(reader):
                print(f"{i+1}. {row['Timestamp']} | {row['Source IP']} -> {row['Destination IP']} | {row['Protocol']}")
                if i == 19:
                    print(Fore.CYAN + "\n...only showing first 20 rows.\n")
                    break
    except FileNotFoundError:
        print(Fore.RED + "No CSV log found. Please run packet sniffing first.")
