from max import max_of

print("Getting the max value of an array.")
print("Caution: program ends when 'End' entered.")

number = 0
x = []

while True:
    s = input(f'Enter the value of x[{number}]:')
    
    if s == "End":
        break
    x.append(s)
    number += 1
    
print(f"{number} numbers are entered.")
print(f"max value is {max_of(x)}.")
