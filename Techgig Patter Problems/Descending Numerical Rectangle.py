#Descending Numerical Rectangle
"""
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(5-j,end=' ')
        else:
            print(5-j,end='')
    if i<n-1:
        print()