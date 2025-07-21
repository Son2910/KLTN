import os
import csv

log_dir = "/home/p4/P4DDoS/simulation_code/quickSimulation/results"
output_csv = "/home/p4/P4DDoS/simulation_code/quickSimulation/metrics.csv"

records = []

for filename in os.listdir(log_dir):
    if filename.endswith(".log"):
        filepath = os.path.join(log_dir, filename)
        with open(filepath, "r") as f:
            lines = f.readlines()

        if len(lines) < 2:
            continue

        # Parse detection list
        try:
            detection_list = eval(lines[0].strip())
        except Exception as e:
            print(f"Error parsing detection list in {filename}: {e}")
            continue

        if not isinstance(detection_list, list):
            print(f"Skipping {filename}: detection_list is not a list")
            continue

        accuracy = float(lines[1].strip())
        tp = sum(detection_list)
        fp = len(detection_list) - tp

        # Parse method and attack proportion from filename
        # Example: p4ddos_botnet_5.log
        parts = filename.replace(".log", "").split("_")
        if len(parts) >= 3:
            method = parts[0]
            attack = parts[2]
        else:
            method = "Unknown"
            attack = "Unknown"

        record = {
            "Attack": attack,
            "Method": method,
            "Accuracy": accuracy,
            "TP": tp,
            "FP": fp
        }
        records.append(record)

with open(output_csv, "w", newline="") as csvfile:
    fieldnames = ["Attack", "Method", "Accuracy", "TP", "FP"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in records:
        writer.writerow(r)

print(f"Done! Extracted {len(records)} records to metrics.csv.")

