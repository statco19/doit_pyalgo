from ssearch_while import seq_search

print("Finding a float.")
print("Caurtion: the program quits when 'End' entered")

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s == "End":
        break
    x.append(float(s))
    number += 1
    
ky = float(input("What to search?: "))

idx = seq_search(x,ky)

if idx == -1:
    print("No such an element")
else:
    print(f"The element is at x[{idx}]")
