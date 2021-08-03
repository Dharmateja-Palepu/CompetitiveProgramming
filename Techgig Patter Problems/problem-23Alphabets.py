"""
E D C B A
E D C B
E D C
E D
E
"""

n=int(input())
for i in range(0,n):
    for j in range(n-i):
        if j<n-1-i:
            print(chr(65+(n-1-j)),end=' ')
        else:
            print(chr(65+(n-1-j)),end='')

    if i<n-1:    
        print()