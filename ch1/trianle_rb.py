n = int(input("type an integer"))

for i in range(n):
    print(' ' * (n-(i+1)), end='')
    print('*' * (i+1), end='')
    print()
