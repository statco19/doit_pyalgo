# generating n random integers between 10 and 99(break if 13 comes out)

import random

n = int(input("How many numbers do you want?: "))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print("\nQuit the program")
        break
else:
    print("\nQuit generating random numbers")
