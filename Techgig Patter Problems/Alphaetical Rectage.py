# Alphaetical Rectage

"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E"""

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(chr(65+i),end=' ')
        else:
            print(chr(65+i),end='')
    if i<n-1:
        print()