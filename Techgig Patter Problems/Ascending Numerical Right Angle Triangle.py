#Ascending Numerical Right Angle Triangle
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 """


n=int(input())
for i in range(0,n):
    for j in range(i+1):
        if j<i:
            print(j+1,end=' ')
        else:
            print(j+1,end='')

    if i<n-1:    
        print()