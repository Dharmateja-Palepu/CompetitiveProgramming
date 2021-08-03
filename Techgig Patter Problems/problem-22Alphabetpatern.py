"""
E E E E E
D D D D
C C C
B B
A 
"""
n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(chr(65+(n-i-1)),end=' ')
        else:
            print(chr(65+(n-i-1)),end='')

    if i<n-1:    
        print()