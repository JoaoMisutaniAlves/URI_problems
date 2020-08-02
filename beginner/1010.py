# -*- coding: utf-8 -*-

product1 = input().split(" ")
product2 = input().split(" ")
_, qtde1, valor1 = product1
_, qtde2, valor2 = product2
TOTAL = ( int( qtde1 ) * float( valor1 ) ) + ( int( qtde2 ) * float( valor2 ) )
print ("VALOR A PAGAR: R$ %.2f"%TOTAL)