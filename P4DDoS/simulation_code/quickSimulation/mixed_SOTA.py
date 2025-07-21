# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: SOTA.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2020-02-24 16:30:26
# ###########################
from collections import Counter


HdstList=[6025, 7719, 8391, 7958, 7958, 7958, 8257, 7849, 7849, 7849, 8089, 7958, 7849, 8089, 7713, 7958, 7958, 8437, 8089, 7713, 6977, 7958, 8089, 8089, 8089, 7958, 7713, 8089, 7997, 8089, 8089, 8257, 7958, 7713, 7958, 7824, 7958, 7958, 8326, 7958, 8257, 8089, 7958, 7958, 7958, 7958, 7958, 7849, 7958, 8528]
HsrcList=[12541, 12879, 12879, 12842, 12842, 12842, 13209, 12397, 13209, 12809, 12825, 12842, 12809, 13209, 12825, 12842, 13202, 12797, 13209, 12825, 12541, 13202, 12825, 13209, 13209, 12474, 12825, 13209, 12797, 13209, 13209, 13209, 13202, 12825, 12842, 12860, 12842, 12474, 12842, 12842, 12809, 12825, 12842, 12842, 12842, 12842, 12842, 12397, 12842, 12860]
k1 = 0.5
k2 = 1.5
k3 = 4.5
k4 = 5.5

Dsrc = 149
Ddst = 102
EWMA_dst = 10479
EWMA_src = 11357
alpha = 0.13
ddos1List = []
ddos2List = []
ddos3List = []
ddos4List = []
for i in range(len(HdstList)):
    ddos1 = 0
    ddos2 = 0
    ddos3 = 0
    ddos4 = 0
    if (HsrcList[i] > EWMA_src+k1*Dsrc or HdstList[i]<EWMA_dst - k1*Ddst):
        ddos1 = 1
    if (HsrcList[i] > EWMA_src+k2*Dsrc or HdstList[i]<EWMA_dst - k2*Ddst):
        ddos2 = 1
    if (HsrcList[i] > EWMA_src+k3*Dsrc or HdstList[i]<EWMA_dst - k3*Ddst):
        ddos3 = 1
    if (HsrcList[i] > EWMA_src+k4*Dsrc or HdstList[i]<EWMA_dst - k4*Ddst):
        ddos4 = 1
    ddos1List.append(ddos1)
    ddos2List.append(ddos2)
    ddos3List.append(ddos3)
    ddos4List.append(ddos4)
    a1 = Counter(ddos1List)
a2 = Counter(ddos2List)
a3 = Counter(ddos3List)
a4 = Counter(ddos4List)
p1 = a1[1]/50
p2 = a2[1]/50
p3 = a3[1]/50
p4 = a4[1]/50
print(p1)
print(p2)
print(p3)
print(p4)

