# -*- coding: utf-8 -*-

order = input().split(" ")
A, B = order
A = int(A)
B = int(B)

if A == 1:
    print("Total: R$ %.2f"%(4.00*B))
if A == 2:
    print("Total: R$ %.2f"%(4.50*B))
if A == 3:
    print("Total: R$ %.2f"%(5.00*B))
if A == 4:
    print("Total: R$ %.2f"%(2.00*B))
if A == 5:
    print("Total: R$ %.2f"%(1.50*B))