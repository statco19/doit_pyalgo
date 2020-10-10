n = int(input("type an integer: "))
"""
for i in range(1,n+1):
    for j in range(i,i+1):
        print('*'*j)
"""
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

