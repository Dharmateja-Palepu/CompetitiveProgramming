# Number pattern Triangle/ problem -30

"""
5 5 5 5 5
   4 4 4 4
      3 3 3
         2 2
            1 
            """

n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=' ')
    for j in range(n-i):
        if j<n-i-1:
            print(n-i,end=' ')
        elif j<n-i:
            print(n-i,end='')
    print()            