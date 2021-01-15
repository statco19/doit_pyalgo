def fsort(a, MAX):
	n = len(a)
	f = [0] * (max(a)+1)
	b = [0] * n
	
	for i in range(n):
		f[a[i]] += 1
		
	for i in range(1, max(a)+1):
		f[i] += f[i-1]
		
	for i in range(n-1,-1,-1):
		f[a[i]] -= 1
		b[f[a[i]]] = a[i]
	
	for i in range(n):
		a[i]=b[i]
		
	return a
	
if __name__ == "__main__":
	a = [22,5,11,32,99,68,70]
	print(fsort(a, max(a)))
