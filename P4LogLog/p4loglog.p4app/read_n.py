from bmv2 import Bmv2SwitchConnection

sw = Bmv2SwitchConnection()
# Kết nối switch, mặc định thrift port 9090
sw.thrift_port = 9090
sw.connect()

# Đọc thanh ghi nReg
entries = sw.register_read("nReg", 0, 1)
n_value = entries[0]
print(f"n = {n_value}")

# Ghi ra file
with open("n_value.txt", "w") as f:
    f.write(str(n_value))
