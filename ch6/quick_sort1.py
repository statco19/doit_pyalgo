def qsort(a, left, right): # left = 0, right = n-1
	n = len(a)
	pl = left
	pr = right
	x = a[(left+right)//2]
	
	while pl <= pr:
		while a[pl] < x: pl += 1
		while a[pr] > x: pr -= 1
		
		if pl <= pr:
			a[pl], a[pr] = a[pr], a[pl]
			pl += 1
			pr -= 1
			
	if left < pr: qsort(a, left, pr)
	if right > pl: qsort(a, pl, right)
	
	return a
def quick_sort(a):
	return qsort(a, 0, len(a)-1)
	
if __name__ == "__main__":
	a = [5,8,4,2,6,1,3,9,7]
	print(quick_sort(a))	
