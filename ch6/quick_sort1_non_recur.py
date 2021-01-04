from stack import Stack

def qsort(a, left, right):
	n = len(a)
	s = Stack(n)
	
	s.push((left,right))
	
	while not s.is_empty():
		#left, right = s.pop()
		#pl, pr = left, right
		
		pl, pr = left, right = s.pop()
		x = a[(left+right)//2]
		
		while pl <= pr:
			while a[pl] < x: pl += 1
			while a[pr] > x: pr -= 1
			
			if pl <= pr:
				a[pl], a[pr] = a[pr], a[pl]
				pl += 1
				pr -= 1
				
		if left < pr: s.push((left, pr))
		if pl < right: s.push((pl, right))
		
	return a
	
if __name__ == "__main__":
	a = [5,8,4,2,6,1,3,9,7]
	print(qsort(a, 0 , len(a)-1))
