# -*- coding: utf-8 -*-
import math

POINT1 = input().split(" ")
x1, y1 = POINT1
POINT2 = input().split(" ")
x2, y2 = POINT2
Distance = math.sqrt( math.pow( ( float(x2) - float(x1) ) , 2 ) + math.pow( ( float(y2) - float(y1) ), 2 ) )
print ("%.4f"%Distance)