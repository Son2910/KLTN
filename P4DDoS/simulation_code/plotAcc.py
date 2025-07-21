# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: logarithm.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2019-07-08 12:14:08
# ###########################


import math
import matplotlib.pyplot as plt
import tikzplotlib



# def plotBits():
    # plt.figure(figsize=(10, 10))
    # plt.rcParams["font.weight"] = "bold"
    # plt.rcParams["axes.labelweight"] = "bold"
    # plt.xlabel(r"$\theta$", fontsize=15)
    # plt.ylabel(r"Detection accuracy for $\eta$", fontsize=15)
    # plt.xticks(fontsize=15)
    # plt.yticks(fontsize=15)
    # # plt.ylim(0, 10)
    # plt.plot(x_1, y_1,  marker='o', mec='r', mfc='w',
             # label=u"$150M$")
    # plt.plot(x_1, y_2, marker='x', mec='r', mfc='w',
             # label=u'$320M$')
    # plt.plot(x_1, y_3,  marker='^', mec='r', mfc='w',
             # label=u"$700M$")
    # plt.plot(x_1, y_4, marker='*', mec='r', mfc='w',
             # label=u'$1G$')
    # plt.plot(x_1, y_5, marker='+', mec='r', mfc='w',
             # label=u'$Mixed$')
    # # plt.axhline(y=1, linestyle='--', color='k')
    # plt.legend(fontsize=20, ncol=2, handleheight=1, labelspacing=0.05)
    # # plt.savefig(str(N2)+"nodes_Recall_"+str(acc)+"avg.png")
    # tikzplotlib.save("sensTheta.tex")
    # plt.show()
    # plt.close()


# x_1 = [0.01, 0.02, 0.03,0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
# y_1 = [1.0, 1.0, 1.0, 0.98, 0.94, 0.94, 0.94, 0.94, 0.86, 0.8]
# y_2 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
# y_3 = [1.0, 1.0, 1.0, 0.98, 0.94, 0.94, 0.94, 0.94, 0.86, 0.8]
# y_4 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
# y_5 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
# plotBits()

def plotNorm():
    plt.figure(figsize=(10, 10))
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.xlabel(r"Attack traffic proportion (\%)", fontsize=15)
    plt.ylabel(r"Detection accuracy (\%)", fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    # plt.ylim(0, 10)
    plt.plot(x_1, y_1,  marker='o', mec='r', mfc='w',
             label=u"P4DDoS")
    plt.plot(x_1, y_2, marker='x', mec='r', mfc='w',
             label=u'SOTA_DDoS (k=3.5)')
    plt.plot(x_1, y_3,  marker='^', mec='r', mfc='w',
             label=u"SOTA_DDoS (k=2.5)")
    plt.plot(x_1, y_4, marker='*', mec='r', mfc='w',
             label=u'SOTA_DDoS (k=1.5)')
    plt.plot(x_1, y_5, marker='+', mec='r', mfc='w',
             label=u'SOTA_DDoS (k=0.5)')
    # plt.axhline(y=1, linestyle='--', color='k')
    plt.legend(fontsize=20, ncol=2, handleheight=1, labelspacing=0.05)
    # plt.savefig(str(N2)+"nodes_Recall_"+str(acc)+"avg.png")
    tikzplotlib.save("BotnetAttack.tex")
    plt.show()
    plt.close()

x_1 = [5, 10, 15, 20, 25, 30]
y_1 = [40, 92, 100, 100, 100, 100]
y_2 = [8, 10, 10, 10, 8, 10]
y_3 = [12, 14, 12, 12, 12, 14]
y_4 = [18, 20, 20, 20, 18, 20]
y_5 = [34, 34, 36, 36, 34, 38]
plotNorm()

