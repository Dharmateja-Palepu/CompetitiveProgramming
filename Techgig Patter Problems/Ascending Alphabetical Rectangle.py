#Ascending Alphabetical Rectangle
"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E 
"""

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(chr(65+j),end=' ')
        else:
            print(chr(65+j),end='')
    if i<n-1:
        print()