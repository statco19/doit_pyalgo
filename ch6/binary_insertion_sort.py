import bisect

def	binary_insertion_sort(a):
	n = len(a)
	
	for i in range(1,n):
		key = a[i]
		pl = 0
		pr = i-1
		
		while True:
			pc = (pl+pr) // 2
			
			if a[pc] == key:
				break
			elif a[pc] < key:
				pl = pc + 1
			else:
				pr = pc - 1
				
			if pl > pr:
				break
				
		pd = pc + 1 if pl <= pr else pr + 1
		
		for j in range(i,pd,-1):
			a[j] = a[j-1]
		a[pd] = key
	
	return a
	
def Bisect(a):
	for i in range(1, len(a)):
		bisect.insort(a,a.pop(i),0,i)
	
	return a

if __name__ == "__main__":
	a = [6,4,8,3,1,9,7]
	print(binary_insertion_sort(a))
	print(Bisect(a))
