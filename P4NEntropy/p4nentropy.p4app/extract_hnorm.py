import re

with open("registers_log.txt", "r") as f:
    content = f.read()

entries = re.findall(r"finalResults= *([0-9,\s]+)", content)

hnorm_values = []
for entry in entries:
    values = [int(x.strip()) for x in entry.split(",")]
    if len(values) >= 5:
        hnorm_values.append(values[4])

for i, v in enumerate(hnorm_values):
    print(f"[{i}] Hnorm = {v} (amplified)")

