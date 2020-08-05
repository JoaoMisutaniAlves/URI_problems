# -*- coding: utf-8 -*-

_, A = input().split(" ")
firstDay = int(A)
B, C, D = input().split(" : ")
firstHour = int(B)
firstMinute = int(C)
firstSecond = int(D)
_, A = input().split(" ")
lastDay = int(A)
B, C, D = input().split(" : ")
lastHour = int(B)
lastMinute = int(C)
lastSecond = int(D)

resulmeDays = lastDay - firstDay

resulmeHours = lastHour - firstHour
if(resulmeHours < 0):
	resulmeHours = 24 + resulmeHours
	resulmeDays = resulmeDays - 1

resulmeMinutes = lastMinute - firstMinute
if(resulmeMinutes < 0):
	resulmeMinutes = 60 + resulmeMinutes
	resulmeHours = resulmeHours - 1

resulmeSeconds = lastSecond - firstSecond
if(resulmeSeconds < 0):
	resulmeSeconds = 60 + resulmeSeconds
	resulmeMinutes = resulmeMinutes - 1

if(resulmeDays <= 0):
	resulmeDays = 0

print("%d dia(s)"%resulmeDays)
print("%d hora(s)"%resulmeHours)
print("%d minuto(s)"%resulmeMinutes)
print("%d segundo(s)"%resulmeSeconds)