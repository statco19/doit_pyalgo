# skipping 8

for i in range(1,12):
    if i == 8:        # inefficient way to skip 8 since I ran 12 tines of if statement just to skip
                      # one number
        continue
    print(i, end=' ')
print()
