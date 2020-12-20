from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
	
	ccnt = 0
	scnt = 0
	n = len(a)
	for i in range(n-1):
		exchange = 0
		print(f'pass {i + 1}')
		for j in range(n-1,i,-1):
			for m in range(0,n-1):
				print(f'{a[m]:2}' + (' ' if m!= j-1 else
														' +' if a[j-1] > a[j] else ' -'), end='')
			print(f'{a[n-1]:2}')
			
			ccnt += 1
			
			if a[j-1] > a[j]:
				a[j-1], a[j] = a[j], a[j-1]
				exchange += 1
				scnt += 1
				
		for m in range(0,n-1):
			print(f'{a[m]:2}', end=' ')
		print(f'{a[n-1]:2}')
		
		if exchange == 0:
			break
			
	print(f'compared {ccnt} times.')
	print(f'exchange {scnt} times.')
			
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
	
	"""
	for i in range(num):
		print(f'x[{i}] = {x[i]}')
	"""
