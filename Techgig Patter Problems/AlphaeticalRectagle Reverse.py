"""
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
"""

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(chr(64+n-i),end=' ')
        else:
            print(chr(64+n-i),end='')
    if i<n-1:
        print()