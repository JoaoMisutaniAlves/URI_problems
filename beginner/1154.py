# -*- coding: utf-8 -*-

x = int(0)
l = []
while x >= 0:
    x = int(input())
    if x >= 0:
        l.append(x)
print("%.2f" % (sum(l)/len(l)))