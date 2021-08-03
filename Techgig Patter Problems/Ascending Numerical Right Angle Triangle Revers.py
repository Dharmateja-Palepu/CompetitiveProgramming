#Ascending Numerical Right Angle Triangle Revers

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 

"""



n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(j+1,end=' ')
        else:
            print(j+1,end='')

    if i<n-1:    
        print()