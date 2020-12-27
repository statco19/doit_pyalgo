def insertion_sort(a):
	n = len(a)
	for i in range(1,n):
		j = i
		tmp = a[i]
		while j>0 and a[j-1]>tmp:
			a[j] = a[j-1]
			j -= 1
		a[j] = tmp
	return a

if __name__ == "__main__":
	a = [6,4,8,3,1,9,7]
	print(insertion_sort(a))
