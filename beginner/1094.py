# -*- coding: utf-8 -*-

ttc = tc = tr = ts = 0
for i in range(int(input())):
    A, B = input().split(" ")
    A = int(A)
    ttc+=A
    if B == "C":
        tc+=A
    elif B == "R":
        tr+=A
    elif B == "S":
        ts+=A
pc = (tc/ttc)*100
pr = (tr/ttc)*100
ps = (ts/ttc)*100
print("Total: %i cobaias"%ttc)
print("Total de coelhos: %i"%tc)
print("Total de ratos: %i"%tr)
print("Total de sapos: %i"%ts)
print("Percentual de coelhos: %.2f %%"%pc)
print("Percentual de ratos: %.2f %%"%pr)
print("Percentual de sapos: %.2f %%"%ps)