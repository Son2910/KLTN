#!/usr/bin/env python3
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
import sys
import subprocess
import re
import math

THRIFT_PORT = 22222
NUM_REGISTERS = 16

def read_hll_registers():
    values = []
    for i in range(NUM_REGISTERS):
        cmd = "echo 'register_read hll_register %d' | simple_switch_CLI --thrift-port %d" % (i, THRIFT_PORT)
        output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        match = re.search(r"hll_register\[\d+\]= (\d+)", output)
        if match:
            v = int(match.group(1))
            values.append(v)
        else:
            values.append(0)
    return values

def estimate_cardinality(M):
    m = len(M)
    alpha_m = 0.673
    Z = sum([2.0 ** (-v) for v in M])
    E = alpha_m * m * m / Z
    return int(E)

if __name__ == "__main__":
    hll = read_hll_registers()
    print("HLL registers:", hll)
    n = estimate_cardinality(hll)
    print("Estimated cardinality n = %d" % n)


