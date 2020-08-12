# -*- coding: utf-8 -*-

N = 1
Inter = 0
Gremio = 0
Empates = 0
grenais = 0
while N == 1:
    grenais+=1
    inter, gremio = input().split(" ")
    inter = float(inter)
    gremio = float(gremio)
    if inter > gremio:
        Inter+=1
    elif inter < gremio:
        Gremio+=1
    else:
        Empates+=1
    print("Novo grenal (1-sim 2-nao)")
    N = int(input())
    if N == 2:
        break
    elif N == 1:
        pass
print("%i grenais"%grenais)
print("Inter:%i"%Inter)
print("Gremio:%i"%Gremio)
print("Empates:%i"%Empates)
if Inter == Gremio:
    print("Nao houve vencedor")
elif Inter > Gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")