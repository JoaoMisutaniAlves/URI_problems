# -*- coding: utf-8 -*-

I = 0
while I < 2.1:
    for J in range(3):
        if I == 0 or I == 1:
            print("I=%d J=%d"%(I,I+J+1))
        elif ( I > 1.9 and round(I) == 2):
            print("I=%d J=%d"%(round(I),I+J+1))
        else:
            print("I=%.1f J=%.1f"%(I,I+J+1))
    I+=0.2