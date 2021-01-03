def shell_sort(a):
	n = len(a)
	h = 1
	
	# the maximum value of h is (n//9)
	while h < n//9:
		h = h*3 + 1
		
	while h > 0:
		for i in range(h,n):
			j = i-h
			tmp = a[i]
			
			while j >= 0 and a[j] > tmp:
				a[j+h] = a[j]
				j -= h
			a[j+h] = tmp
			
		h //= 3
		
	return a
	
if __name__ == "__main__":
	a = [8,1,4,2,7,6,3,5]
	print(shell_sort(a))
