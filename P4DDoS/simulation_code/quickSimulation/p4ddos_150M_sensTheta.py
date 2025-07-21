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

Hnorm = [590, 663, 675, 663, 604, 640, 640, 604, 640, 699, 663, 699, 663, 663, 699, 626, 663, 699, 663, 626, 699, 626, 626, 663, 699, 663, 626, 710, 663, 626, 626, 699, 663, 699, 699, 663, 626, 663, 663, 626, 663, 626, 626, 663, 663, 626, 663, 626, 626, 590]
nsrcList =[26170, 35037, 34783, 34326, 34707, 33818, 33411, 33995, 33335, 34885, 34148, 32242, 33767, 34859, 34402, 35596, 34122, 33919, 33919, 34351, 29854, 34656, 33614, 32496, 33157, 33259, 33868, 33843, 34097, 34199, 33513, 33233, 33868, 33792, 33538, 33640, 33614, 33894, 34402, 34377, 34097, 33665, 32496, 34021, 34351, 33386, 33157, 33919, 34402, 34681]

ndstList = [16464, 22117, 23731, 23527, 23896, 23604, 23947, 24861, 23845, 23388, 22892, 22155, 22308, 23426, 22486, 23070, 22892, 22752, 22727, 23273, 19335, 22511, 22854, 23222, 21685, 23311, 22575, 23667, 23184, 22689, 22155, 22663, 23324, 22803, 22206, 21927, 21723, 21495, 23197, 22829, 22308, 22371, 23540, 23184, 23019, 23273, 22143, 22409, 22892, 22663]
theta = 0.09
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

