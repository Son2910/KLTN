with open("/home/p4/P4LogLog/p4loglog.p4app/registers_log.txt") as f:
    lines = f.readlines()

n_values = []
for line in lines:
    if "hash_register=" in line:
        try:
            parts = line.strip().split("=")[1].strip().split(",")
            n = int(parts[2])
            n_values.append(n)
        except:
            continue

if n_values:
    print("Max n =", max(n_values))
else:
    print("Không tìm thấy giá trị n")

