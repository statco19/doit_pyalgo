def partition(a):
	n = len(a)
	pl = 0
	pr = n - 1
	x = a[n//2]
	
	while pl <= pr:
		while a[pl] < x: pl += 1
		while a[pr] > x: pr -= 1
		
		if pl <= pr:
			a[pl], a[pr] = a[pr], a[pl]
			pl += 1
			pr -= 1
			
	return a
	
if __name__ == "__main__":
	a = [1,8,7,4,5,2,6,3,9]
	b = [1,2,3,4,5,6,7,8]
	print(partition(a))
	print(partition(b))
