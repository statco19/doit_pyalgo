# Euclidean algorithm
import math

def GCD(x: int, y: int) -> int:
	return math.gcd(x,y)

def gcd(x: int, y: int) -> int:
	if y == 0:
		return x
	else:
		return gcd(y,x%y)

if __name__ == "__main__":
	print("Evaluating the gcd of two integers.")
	x = int(input("Enter the first integer.: "))
	y = int(input("Enter the second integer: "))
	
	print(f'The gcd is {gcd(x,y)}.')
	print(GCD(x,y))
