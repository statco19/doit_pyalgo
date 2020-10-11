import random
from max import max_of

print("Getting the max value of random integers: ")
n = int(input("Enter the number of random integers: "))
lo = int(input("Enter the min value of random integers: "))
hi = int(input("Enter the max value of random integers: "))

x=[]
for i in range(n):
    x.append(random.randint(lo,hi))

print(x)
print(f"The max value is {max_of(x)}.")
