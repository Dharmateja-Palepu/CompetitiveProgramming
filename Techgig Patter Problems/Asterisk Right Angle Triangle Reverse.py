#Asterisk Right Angle Triangle Reverse
"""
* * * * *
* * * *
* * *
* *
* 

"""
n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-i-1:
            print("*",end=' ')
        else:
            print("*",end='')

    if i<n-1:    
        print()