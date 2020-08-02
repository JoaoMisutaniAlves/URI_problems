# -*- coding: utf-8 -*-

days = int(input())
print("%d ano(s)" %( days // 365 ))
print("%d mes(es)" %( days % 365 // 30 ))
print("%d dia(s)" %( days % 365 % 30 ))