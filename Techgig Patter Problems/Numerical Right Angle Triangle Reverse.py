#Numerical Right Angle Triangle Reverse
"""
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5 


"""
n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(i+1,end=' ')
        else:
            print(i+1,end='')

    if i<n-1:    
        print()