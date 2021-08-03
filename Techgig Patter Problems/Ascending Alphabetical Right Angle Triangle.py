#Ascending Alphabetical Right Angle Triangle
"""
A
A B
A B C
A B C D
A B C D E 


"""
n=int(input())
for i in range(0,n):
    for j in range(i+1):
        if j<i:
            print(chr(65+j),end=' ')
        else:
            print(chr(65+j),end='')

    if i<n-1:    
        print()