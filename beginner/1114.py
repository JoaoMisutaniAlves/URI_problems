# -*- coding: utf-8 -*-

password = 0
result = []
while password != 2002:
    password = int(input())
    if password != 2002:
        result.append("Senha Invalida")
    else:
        result.append("Acesso Permitido")
for i in result:
    print(i)