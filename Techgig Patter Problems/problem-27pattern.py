"""
       A
      B B
    C C C
  D D D D
E E E E E 
"""

n= int(input())
for i in range(n):
    for j in  range(1,n-i):
        print(" ",end=' ')
    for j in range(i+1):
        if j<i:
            print(chr(65+i),end=' ')
        else:
            print(chr(65+i),end='')
    if i<n:
        print()
        