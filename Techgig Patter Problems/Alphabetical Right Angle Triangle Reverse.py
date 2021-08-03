#Alphabetical Right Angle Triangle Reverse
"""
A A A A A
B B B B
C C C
D D
E 
"""


n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(chr(65+i),end=' ')
        else:
            print(chr(65+i),end='')

    if i<n-1:    
        print()