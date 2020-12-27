def selection_sort(a):
	n = len(a)
	
	for i in range(n-1):
		min = i
		for j in range(i+1,n):
			if a[j] < a[min]:
				min = j
		a[i], a[min] = a[min], a[i]
	return a
		
if __name__ == "__main__":
	a = [6,4,8,3,1,9,7]
	print(selection_sort(a))
