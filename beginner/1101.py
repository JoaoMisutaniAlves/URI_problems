# -*- coding: utf-8 -*-

def print_in_line(list_range):
    a = ""
    for i in list_range:
        a = a +"%i " %i
    print(a + "Sum=%i"%sum(list_range))


A, B = input().split(" ")
A = int(A)
B = int(B)
result = []
while A > 0 and B > 0:
    if A > B:
        list_to_sum = range(B, A+1)
    else:
        list_to_sum = range(A, B+1)
    result.append(list_to_sum)
    A, B = input().split(" ")
    A = int(A)
    B = int(B)
for i in result:
    print_in_line(i)