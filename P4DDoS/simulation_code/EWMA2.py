# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: entropyES.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2019-07-20 16:58:52
# ###########################

from countsketch import CountSketch
import math
from tqdm import tqdm
from hashlib import md5
import gmpy



def log2ES(x, m, pre):
    w = x | (x >> 1)
    w = w | (w >> 2)
    w = w | (w >> 4)
    w = w | (w >> 8)
    w = w | (w >> 16)
    w = w | (w >> 32)
    b = (w & 0x5555555555555555) + ((w >> 1) & 0x5555555555555555)
    b = (b & 0x3333333333333333) + ((b >> 2) & 0x3333333333333333)
    b = (b & 0x0f0f0f0f0f0f0f0f) + ((b >> 4) & 0x0f0f0f0f0f0f0f0f)
    b = (b & 0x00ff00ff00ff00ff) + ((b >> 8) & 0x00ff00ff00ff00ff)
    b = (b & 0x0000ffff0000ffff) + ((b >> 16) & 0x0000ffff0000ffff)
    b = (b & 0x00000000ffffffff) + ((b >> 32) & 0x00000000ffffffff)
    n = b - 1
    if n - m < 0:
        k = x - (1 << n)
        n_b = 1 << n
    else:
        k = ((x - (1 << n)) >> (n-m))
        n_b = (((1 << m)))
    log2x = n*1024 + int(round(math.log2(1 + (k/n_b)), pre) *1024)
    return log2x


def expES(x, d, m, terms, decimal_pre):
    bEXP = int(d * (log2ES(x, m, decimal_pre)))
    exp_int = int(bEXP/1024)
    exp_decimal = int(bEXP - (exp_int << 10))
    i = 0
    a = exp_decimal
    # 1 means 2 terms
    # 6 means 7 terms
    while(i < terms):
        if i == 0:
            two_to_decimal = (1 << 10) + exp_decimal
        else:
            a = (a * (1024*i - exp_decimal)/1024)
            b = int(a/math.factorial(i+1))
            if i % 2 == 1:
                two_to_decimal -= int(b)
            else:
                two_to_decimal += int(b)
        i += 1
    if exp_int > 10:
        expResult = (1<<(exp_int - 10)) * two_to_decimal
    else:
        expResult = (((1 << exp_int) * two_to_decimal)/1024)
    return expResult


class Switch(object):
    def __init__(self, Nh, m):
        self.Stot = 0
        self.Sum2 = 0
        self.Sum = 0
        self.Nh = Nh
        self.cs = CountSketch(Ns, self.Nh)
        self.cs2 = CountSketch(Ns, self.Nh)
        self.ll_src = LogLog(m)
        self.ll_dst = LogLog(m)

    def add(self, srcdst):
        self.Stot += 1
        srcdstlist = srcdst.split(" ")
        src = srcdstlist[0]
        dst = srcdstlist[1]
        self.ll_src.update(src)
        self.ll_dst.update(dst)
        self.cs.add(dst)
        self.cs2.add(src)
        count = self.queryCount(dst)
        count2 = self.queryCount2(src)
        if count > 1:
            self.Sum += log2ES(int(count), N_bits, 3) + int(1.44 * 1024)
        if count2 > 1:
            self.Sum2 += log2ES(int(count2), N_bits, 3) + int(1.44 * 1024)

    def queryCount(self, srcdst):
        return self.cs.query(srcdst)

    def queryCount2(self, srcdst):
        return self.cs.query(srcdst)

    def queryNsrc(self):
        return int(self.ll_src.query())

    def queryNdst(self):
        return int(self.ll_dst.query())

    def querySum(self):
        return self.Sum

    def querySum2(self):
        return self.Sum2


    def queryStot(self):
        return self.Stot





def traffic(switchID, window):
    f = open(str(window)+'sF.txt', 'r')
    lines = f.readlines()
    flowDit = {}
    for x in tqdm(range(0, len(lines))):
        switchID.add(lines[x])
    return switchID

class LogLog(object):
    def __init__(self, m):
        self.m = m
        self.reg = [0]*(self.m)
        self.occ = 0
        self.alpha_m = 0.3970

    def update(self, x):
        md = md5()
        md.update(str(x).encode("UTF-8"))
        h = int(md.hexdigest(), 16)
        buc = h & (self.m - 1)
        hv = h >> int(math.log2(self.m))
        lsb = gmpy.scan1(hv) + 1
        if self.reg[buc] < lsb and self.reg[buc] == 0:
            self.occ +=1
            self.reg[buc] = lsb
        elif self.reg[buc] < lsb:
            self.reg[buc] = lsb

    def query(self):
        e = self.alpha_m * self.m * expES(2, (sum(self.reg)/self.m), 4, 6, 3)
        # e = self.alpha_m * self.m * 2**(sum(self.reg)/self.m)
        if e <= 2.5*self.m and self.occ < self.m:
            return (self.m * log2ES(self.m, 4, 3) - self.m * log2ES((self.m - self.occ),4, 3))/1024
        else:
            return e

# Count-min sketch output size
# Ns = 100000
# Count-min sketch number of hash functions
Ns = 2000

m = 2048
N_bits = 4
NhList = [5]
HsrcList = []
HdstList = []
srcList = []
dstList = []
# alpha_list = [0.2, 0.4, 0.6, 0.8]
alpha_list = [0.13]
normDict = {}
srcDict ={}
dstDict = {}
alpha = 0.13

for i in range(0, 50, 1):
    switch1 = Switch(Nh, m)
    switch1 = traffic(switch1, i)
    Stot = switch1.queryStot()
    Sum = switch1.querySum()
    Sum2 = switch1.querySum2()
    ndst = switch1.queryNdst()
    nsrc = switch1.queryNsrc()
    srcList.append(nsrc)
    dstList.append(ndst)
    if Sum >= Stot:
        exp = (log2ES(int(Sum), N_bits, 3) - \
           log2ES(int(Stot), N_bits, 3))/1024 -10
        H2 = expES(2, exp, 4, 6, 3)
    else:
        H2 = 0
    # H amplified 2^10
    Hdst = int((log2ES(Stot, N_bits, 3)  - (H2*1024)))

    if Sum2 >= Stot:
        exp = (log2ES(int(Sum2), N_bits, 3) - \
           log2ES(int(Stot), N_bits, 3))/1024 -10
        H_src = expES(2, exp, 4, 6, 3)
    else:
        H_src = 0
    # H amplified 2^10
    Hsrc = int((log2ES(Stot, N_bits, 3)  - (H_src*1024)))
    HsrcList.append(Hsrc)
    HdstList.append(Hdst)
    print(HdstList)
    print(HsrcList)
