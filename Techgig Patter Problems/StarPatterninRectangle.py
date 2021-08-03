# Astreik rectangle / Star Pattern

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *  """

n= int(input())
for i in range(n):
    for j in range(0,5):
        if j<4:
            print('*',end=' ')
        else:
            print('*',end='')
        
    if i<n-1:
        print()