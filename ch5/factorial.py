import math

def fac(n: int) -> int:
	return math.factorial(n)
	
def factorial(n: int) -> int:
	if n > 0:
		return n * factorial(n-1)
	else:
		return 1
		
if __name__ == "__main__":
	n = int(input("Enter integer: "))
	print(f"{n}'s factorial is {factorial(n)}.")
	print(fac(n))
