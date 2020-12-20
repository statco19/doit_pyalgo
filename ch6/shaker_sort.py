from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
	
	left = 0
	right = len(a) - 1
	last = right
	
	while left < right:
		for j in range(right, left, -1):
			if a[j-1] > a[j]:
				a[j-1], a[j] = a[j], a[j-1]
				last = j
		left = last
				
		for j in range(left, right):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				last = j
		right = last
				
if __name__ == "__main__":
	print("Commiting the bubble sorting.")
	# num = int(input("Enter the number of elements: "))
	x = [6,4,3,7,1,9,8]
	num = len(x)
	
	"""
	for i in range(num):
		x[i] = int(input(f'x[{i}]: '))
	"""
	shaker_sort(x)
	print("Ascending order complete.")
	
	
	for i in range(num):
		print(f'{x[i]}', end = ' ')
