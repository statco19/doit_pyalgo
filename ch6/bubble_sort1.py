from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
	n = len(a)
	"""
	for i in range(n-1):
		# pass
		for j in range(n-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	"""
	for i in range(n-1):
		for j in range(n-1,i,-1):
			if a[j-1] > a[j]:
				a[j-1], a[j] = a[j], a[j-1]

if __name__ == "__main__":
	print("Commiting the bubble sorting.")
	num = int(input("Enter the number of elements: "))
	x = [None] * num
	
	for i in range(num):
		x[i] = int(input(f'x[{i}]: '))
		
	bubble_sort(x)
	print("Ascending order complete.")
	
	for i in range(num):
		print(f'x[{i}] = {x[i]}')
				
