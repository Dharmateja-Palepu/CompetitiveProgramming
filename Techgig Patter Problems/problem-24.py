"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        if j<i:
            print('*',end=' ')
        else:
            print('*',end='')
    if i<n-1:
        print()