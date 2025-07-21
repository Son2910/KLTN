# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: SOTA.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2020-02-24 16:30:26
# ###########################
from collections import Counter


HdstList = [8225, 9353, 9833, 9353, 9152, 9672, 9672, 9152, 9672, 10016, 9353, 9816, 9672, 9672, 10016, 9152, 9672, 10184, 9672, 8873, 9759, 9152, 9152, 9456, 9816, 9353, 9152, 10376, 9288, 9152, 9152, 9816, 9672, 9816, 9816, 9353, 9152, 9353, 9353, 9152, 9353, 8873, 9152, 9353, 9353, 8873, 9672, 9152, 9152, 8646]
HsrcList = [12565, 12309, 12309, 12541, 12532, 12532, 12788, 12280, 12788, 12784, 12541, 12256, 12788, 13036, 12516, 12532, 12788, 12788, 12532, 12541, 12531, 12532, 12532, 12784, 12784, 12541, 12788, 12784, 12784, 12788, 12532, 12524, 12788, 12524, 12524, 12541, 12280, 12309, 12541, 12024, 12541, 12309, 11776, 12309, 12541, 12541, 12280, 12280, 12280, 12342]

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

    print("========")
    print(HsrcList[i])
    print(EWMA_src+k4*Dsrc)
    print(HdstList[i])
    print(EWMA_dst-k4*Ddst)
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

