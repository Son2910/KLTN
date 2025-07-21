import subprocess
import re
import csv

# Danh sách script cần chạy và mô tả Attack traffic %
# (Bạn sửa tên file theo thực tế folder của bạn)
scripts = [
    ("p4ddos_botnet_5.py", 5, "P4DDoS"),
    ("p4ddos_botnet_10.py",10, "P4DDoS"),
    ("p4ddos_botnet_15.py",15, "P4DDoS"),
    ("p4ddos_botnet_20.py",20, "P4DDoS"),
    ("p4ddos_botnet_25.py",25, "P4DDoS"),
    ("p4ddos_botnet_30.py",30, "P4DDoS"),
    ("SOTA_5.py",5, "SOTA"),
    ("SOTA_10.py",10, "SOTA"),
    ("SOTA_15.py",15, "SOTA"),
    ("SOTA_20.py",20, "SOTA"),
    ("SOTA_25.py",25, "SOTA"),
    ("SOTA_30.py",30, "SOTA"),
]

# Lưu kết quả tại đây
results = []

for script, attack, method in scripts:
    print(f"Running {script}...")
    try:
        # Chạy script và lấy output
        proc = subprocess.run(
            ["python3", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            timeout=120  # Giới hạn thời gian chạy 2 phút
        )
        output = proc.stdout.strip()
        print(output)

        # Tìm số cuối cùng trong output (accuracy)
        numbers = re.findall(r"[0-9]*\.?[0-9]+", output)
        if not numbers:
            accuracy = ""
            print(f"❌ Không tìm thấy số nào trong output!")
        else:
            accuracy = numbers[-1]
            print(f"✅ Accuracy = {accuracy}")

        # Lưu kết quả
        results.append({
            "Attack": attack,
            "Method": method,
            "Accuracy": accuracy
        })

    except Exception as e:
        print(f"❌ Lỗi khi chạy {script}: {e}")
        results.append({
            "Attack": attack,
            "Method": method,
            "Accuracy": ""
        })

# Ghi ra CSV
with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Attack","Method","Accuracy"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("\n✅ DONE. Kết quả lưu trong results.csv")
