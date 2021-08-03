#Asterisk Right Angle Triangle
"""
*
* *
* * *
* * * *
* * * * *
"""


n=int(input())
for i in range(0,n):
    for j in range(i+1):
        if j<i:
            print('*',end=' ')
        else:
            print('*',end='')

    if i<n-1:    
        print()