def shell_sort(a):
	n = len(a)
	h=n//2
	
	while h > 0:
		for i in range(h,n):
			j = i-h
			tmp = a[i]
			
			while j>=0 and a[j] > tmp:
				a[j+h] = a[j]
				j -= h
			a[j+h] = tmp
			
		h //= 2
		
	return a

if __name__ == "__main__":
	a = [8,1,4,2,7,6,3,5]
	print(shell_sort(a))
