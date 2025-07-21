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

EWMA =727
alpha = 0.13
ewma_eta = 273

Hnorm = [551, 626, 604, 626, 640, 640, 675, 675, 675, 663, 663, 626, 699, 699, 699, 626, 663, 735, 699, 699, 626, 663, 699, 699, 699, 663, 663, 675, 699, 699, 699, 735, 663, 699, 626, 663, 626, 663, 626, 626, 699, 663, 675, 699, 663, 626, 663, 663, 626, 663]
nsrcList = [20402, 28558, 29015, 28406, 28584, 27847, 27567, 27999, 27440, 28990, 28075, 27466, 27643, 28507, 28634, 29422, 28050, 27872, 27923, 28202, 25344, 28761, 27694, 27135, 27745, 27694, 27923, 28228, 28025, 28253, 27745, 28075, 28075, 28304, 28329, 27897, 27974, 28253, 28050, 28609, 27872, 27770, 27923, 28177, 28177, 27567, 27720, 28355, 28584, 28812]
ndstList = [16477, 22143, 23731, 23540, 23896, 23629, 23947, 24849, 23845, 23413, 22892, 22155, 22308, 23426, 22486, 23070, 22918, 22752, 22727, 23299, 19348, 22524, 22879, 23261, 21698, 23349, 22600, 23692, 23197, 22702, 22181, 22663, 23362, 22829, 22219, 21965, 21723, 21533, 23222, 22854, 22320, 22371, 23553, 23197, 23019, 23273, 22155, 22435, 22918, 22689]
theta = 0.0001
theta1 = 0.1
theta2 = 0.07
theta3 = 0.08

ddosList = []
ddosList1 = []
ddosList2 = []
ddosList3 = []
for i in range(0, 50):
    ddos = 0
    ddos1 = 0
    ddos2 = 0
    ddos3 = 0
    nsrc = nsrcList[i]
    ndst = ndstList[i]
    eta = log2ES(nsrc) - log2ES(ndst)
    if (eta > math.log2(1+theta)*1024+ewma_eta):
        ddos = 1
    if (eta > math.log2(1+theta1)*1024+ewma_eta):
        ddos1 = 1
    if (eta > math.log2(1+theta2)*1024+ewma_eta):
        ddos2 = 1
    if (eta > math.log2(1+theta3)*1024+ewma_eta):
        ddos3 = 1
    ddosList.append(ddos)
    ddosList1.append(ddos1)
    ddosList2.append(ddos2)
    ddosList3.append(ddos3)
a1 = Counter(ddosList)
a2 = Counter(ddosList1)
a3 = Counter(ddosList2)
a4 = Counter(ddosList3)
p1 = a1[1]/50
p2 = a2[1]/50
p3 = a3[1]/50
p4 = a4[1]/50
print(p1)
print(p2)
print(p3)
print(p4)

