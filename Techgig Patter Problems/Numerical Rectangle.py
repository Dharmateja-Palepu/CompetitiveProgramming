#1. Numerical Rectangle/Ascending Number

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5 """

n=int(input())
for i in range(0,n):
    for j in range(0,5):
        if j<4:
            print(i+1,end=' ')
        else:
            print(i+1,end='')
    if i<n-1:
        print()