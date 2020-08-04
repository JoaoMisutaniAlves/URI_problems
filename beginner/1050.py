# -*- coding: utf-8 -*-

DDD = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}
A = int(input())
try:
    city = DDD.get(A)
except:
    pass
if city != None:
    print("%s"%city)
else:
    print("DDD nao cadastrado")