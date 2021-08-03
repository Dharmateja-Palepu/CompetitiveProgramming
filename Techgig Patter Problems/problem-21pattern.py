#Pattern Problem - 21
"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5 
"""
n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(n-j,end=' ')
        else:
            print(n-j,end='')

    if i<n-1:    
        print()