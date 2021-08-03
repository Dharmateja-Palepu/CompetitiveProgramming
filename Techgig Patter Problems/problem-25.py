"""
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5 
"""

n= int(input())
for i in range(n):
    for j in  range(0,n-i):
        print(" ",end=' ')
    for j in range(i+1):
        if j<i:
            print(i+1,end=" ")
        else:
            print(i+1,end="")
    if i<n:
        print()
        
