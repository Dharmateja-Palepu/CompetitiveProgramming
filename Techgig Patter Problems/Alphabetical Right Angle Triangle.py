#Alphabetical Right Angle Triangle
"""
A
B B
C C C
D D D D
E E E E E 


"""
n=int(input())
for i in range(0,n):
    for j in range(i+1):
        if j<i:
            print(chr(65+i),end=' ')
        else:
            print(chr(65+i),end='')

    if i<n-1:    
        print()