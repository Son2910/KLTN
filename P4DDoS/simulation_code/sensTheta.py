# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: cal.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2020-01-21 17:50:23
# ###########################

import math
from collections import Counter

def log2ES(x):
    m = 4
    pre =3
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

Hnorm = [699, 735, 710, 771, 710, 710, 710, 710, 745, 771, 735, 735, 735, 771, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 710, 771, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 735, 699]

EWMA =0
alpha = 0.13

theta = 0.01
theta1 = 0.02
theta2 = 0.03
theta3 = 0.04
theta4 = 0.05
theta5 = 0.06
theta6 = 0.07
theta7 = 0.08
theta8 = 0.09
theta9 = 0.1


nsrcList =[19805, 27847, 28177, 27821, 28025, 27262, 27135, 27491, 26881, 28584, 27618, 26729, 27084, 27770, 27923, 28761, 27440, 27491, 27339, 27720, 24556, 28075, 27084, 26424, 27110, 26907, 27389, 27694, 27440, 27720, 26856, 27339, 27237, 27466, 27389, 27084, 27135, 27491, 27440, 27618, 27313, 27110, 26856, 27237, 27339, 26780, 26983, 27618, 27567, 27643]
ndstList = [16451, 22117, 23718, 23502, 23870, 23591, 23947, 24849, 23845, 23362, 22892, 22155, 22270, 23413, 22486, 23045, 22892, 22752, 22727, 23273, 19335, 22511, 22854, 23222, 21685, 23311, 22575, 23667, 23184, 22663, 22155, 22651, 23324, 22803, 22193, 21927, 21723, 21495, 23197, 22829, 22308, 22371, 23540, 23184, 23019, 23261, 22143, 22409, 22892, 22663]

ewma = 0
ddosList = []
ddosList1 = []
ddosList2 = []
ddosList3 = []
ddosList4 = []
ddosList5 = []
ddosList6 = []
ddosList7 = []
ddosList8 = []
ddosList9 = []
for i in range(0, 50):
    ddos = 0
    ddos1 = 0
    ddos2 = 0
    ddos3 = 0
    ddos4 = 0
    ddos5 = 0
    ddos6 = 0
    ddos7 = 0
    ddos8 = 0
    ddos9 = 0
    nsrc = nsrcList[i]
    ndst = ndstList[i]
    eta = log2ES(nsrc) - log2ES(ndst)
    if i == 0:
        ewma = eta
    else:
        ewma = alpha * eta + (1-alpha)*ewma
    if (eta > math.log2(1+theta)*1024+ewma):
        ddos = 1
    if (eta > math.log2(1+theta1)*1024+ewma):
        ddos1 = 1
    if (eta > math.log2(1+theta2)*1024+ewma):
        ddos2 = 1
    if (eta > math.log2(1+theta3)*1024+ewma):
        ddos3 = 1
    if (eta > math.log2(1+theta4)*1024+ewma):
        ddos4 = 1
    if (eta > math.log2(1+theta5)*1024+ewma):
        ddos5 = 1
    if (eta > math.log2(1+theta6)*1024+ewma):
        ddos6 = 1
    if (eta > math.log2(1+theta7)*1024+ewma):
        ddos7 = 1
    if (eta > math.log2(1+theta8)*1024+ewma):
        ddos8 = 1
    if (eta > math.log2(1+theta9)*1024+ewma):
        ddos9 = 1
    ddosList.append(ddos)
    ddosList1.append(ddos1)
    ddosList2.append(ddos2)
    ddosList3.append(ddos3)
    ddosList4.append(ddos4)
    ddosList5.append(ddos5)
    ddosList6.append(ddos6)
    ddosList7.append(ddos7)
    ddosList8.append(ddos8)
    ddosList9.append(ddos9)
    a1 = Counter(ddosList)
    a2 = Counter(ddosList1)
    a3 = Counter(ddosList2)
    a4 = Counter(ddosList3)
    a5 = Counter(ddosList4)
    a6 = Counter(ddosList5)
    a7 = Counter(ddosList6)
    a8 = Counter(ddosList7)
    a9 = Counter(ddosList8)
    a10 = Counter(ddosList9)
    p1 = a1[1]/50
    p2 = a2[1]/50
    p3 = a3[1]/50
    p4 = a4[1]/50
    p5 = a5[1]/50
    p6 = a6[1]/50
    p7 = a7[1]/50
    p8 = a8[1]/50
    p9 = a9[1]/50
    p10 = a10[1]/50
    plist =[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
print(plist)
