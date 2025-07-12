import matplotlib.pyplot as plt
import csv
from collections import Counter

CSV_FILE = "packet_log.csv"

def plot_protocol_summary():
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            protocols = [row["Protocol"] for row in reader]

        if not protocols:
            print("No data to plot.")
            return

        counts = Counter(protocols)

        # Plotting
        plt.figure(figsize=(6, 4))
        plt.bar(counts.keys(), counts.values(), color='skyblue')
        plt.title("Protocol Distribution")
        plt.xlabel("Protocol")
        plt.ylabel("Count")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("packet_log.csv not found.")
