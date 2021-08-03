#Numerical Rectangle Reverse
"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1 
"""

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(n-i,end=' ')
        else:
            print(n-i,end='')
    if i<n-1:
        print()