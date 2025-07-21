# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: entropy.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2020-01-23 12:29:48
# ###########################
from collections import Counter

HdstList=[10192, 10214, 10526, 10738, 10693, 10693, 10596, 10373, 10956, 10956, 10434, 10434, 10596, 10956, 10596, 10693, 10596, 10596, 10693, 10693, 10569, 10693, 10596, 10539, 10596, 10434, 10292, 10596, 10956, 10596, 10596, 10373, 10693, 10596, 10693, 10434, 10373, 10526, 10434, 10434, 10373, 10214, 10214, 10526, 10526, 10434, 10434, 10373, 10373, 10016]
HsrcList= [11232, 11678, 11678, 11930, 11917, 11917, 11880, 11613, 11880, 12196, 11654, 11930, 11880, 12196, 11880, 11917, 11880, 11880, 11917, 11917, 11785, 11917, 11880, 11875, 11880, 11654, 11880, 11880, 12196, 11880, 11880, 11917, 11917, 11880, 11917, 11654, 11613, 11678, 11654, 11654, 11613, 11678, 11398, 11678, 11966, 11654, 11654, 11613, 11613, 11168]

k1 = 0.5
k2 = 1.5
k3 = 2.5
k4 = 3.5

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
    print(ddos4List)
    EWMA_dst = alpha * (HdstList[i]) + (1-alpha) * EWMA_dst
    Ddst = alpha * abs(EWMA_dst - HdstList[i]) + (1-alpha)*Ddst
    EWMA_src = alpha * (HsrcList[i]) + (1-alpha) * EWMA_src
    Dsrc = alpha * abs(EWMA_src - HsrcList[i]) + (1-alpha)*Dsrc

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
