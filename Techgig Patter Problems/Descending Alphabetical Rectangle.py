#Descending Alphabetical Rectangle
"""
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
"""

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(chr(64+5-j),end=' ')
        else:
            print(chr(64+5-j),end='')
    if i<n-1:
        print()