def max3(a,b,c):
		"return maximun among a,b,c"
		maximum = a
		if b > maximum: maximum = b
		if c > maximum: maximum = c
		return  maximum

print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,2) = {max3(3,2,2)}')
