# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: SOTA.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2020-02-24 16:30:26
# ###########################
from collections import Counter

HdstList=[9446, 9816, 10184, 10016, 10214, 10214, 10214, 10584, 10146, 10146, 10016, 10016, 10146, 10146, 9818, 10584, 10214, 10526, 10214, 10584, 9534, 10214, 10214, 10434, 10214, 10016, 10214, 10214, 10434, 10146, 10146, 10214, 10214, 10146, 10214, 10016, 10214, 10376, 10016, 10016, 10214, 9816, 10184, 10376, 10376, 10016, 10016, 10214, 10584, 9672]
HsrcList=[11990, 12000, 12280, 12256, 12238, 12238, 12510, 12256, 12510, 12510, 11972, 12256, 12226, 12510, 12226, 12516, 12510, 12510, 12238, 12256, 12178, 12238, 12510, 12510, 12510, 11972, 12510, 12510, 12510, 12226, 12226, 12238, 12238, 12226, 12238, 11972, 11966, 12000, 11972, 11972, 11966, 12000, 12024, 12000, 12256, 11972, 11972, 11966, 12256, 11524]

k1 = 0.5
k2 = 1.5
k3 = 4.5
k4 = 5.5

Dsrc = 151
Ddst = 123
EWMA_dst = 10377
EWMA_src = 11620
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
print(ddos1List)
print(ddos2List)
print(ddos3List)
print(ddos4List)

