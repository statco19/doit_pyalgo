from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
	
	n = len(a)
	k = 0
	ccnt = 0
	scnt = 0
	PASS = 0
	
	while k < n-1:
		last = n - 1
		
				
		for j in range(n-1,k,-1):
			if a[j-1] > a[j]:
				a[j-1], a[j] = a[j], a[j-1]
				last = j
				scnt += 1
					
		k = last
	
if __name__ == "__main__":
	print("Commiting the bubble sorting.")
	# num = int(input("Enter the number of elements: "))
	x = [6,4,3,7,1,9,8]
	num = len(x)
	
	"""
	for i in range(num):
		x[i] = int(input(f'x[{i}]: '))
	"""
	bubble_sort(x)
	print("Ascending order complete.")
	
	
	for i in range(num):
		print(f'{x[i]}', end = ' ')

