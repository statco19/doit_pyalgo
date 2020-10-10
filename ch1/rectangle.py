area = int(input("Type the area of a rectangle: "))

for i in range(1, int(area**0.5)): # for loop until the square root of area
    if area % i: 
        continue
    print(f"{i} x {area // i}")
