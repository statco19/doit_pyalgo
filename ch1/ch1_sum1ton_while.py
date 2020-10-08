print("sum from 1 to n.")

n = int(input("type an integer: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
    
print(f'The total sum from 1 to {n} is {sum}.')
