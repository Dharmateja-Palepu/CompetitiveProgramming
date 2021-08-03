#Ascending Alphabetical Right Angle Triangle Reverse
"""
A B C D E
A B C D
A B C
A B
A 
"""

n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(chr(65+j),end=' ')
        else:
            print(chr(65+j),end='')

    if i<n-1:    
        print()