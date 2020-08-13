# -*- coding: utf-8 -*-

X,Y=input().split()
X=int(X)
Y=int(Y)
count=0
while count < Y:
    line = ""
    for j in range(X):
        count+=1
        if (j + 1) == X:
            line+=str(count)
        else:
            line+=str(count)+" "
            if count == Y:
                break
    print(line)