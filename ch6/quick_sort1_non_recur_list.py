def quick_sort(a, left, right):
	st = []
	
	st.append((left,right))
	
	while st:
		pl, pr = left, right = st.pop()
		x = a[(left + right)//2]
		
		while pl <= pr:
			while a[pl] < x: pl += 1
			while a[pr] > x: pr -= 1
			
			if pl <= pr:
				a[pl], a[pr] = a[pr], a[pl]
				pl += 1
				pr -= 1
				
		if left < pr: st.append((pr, right))
		if pl < right: st.append((left, pl))
		
	return a
		
if __name__ == "__main__":
	a = [5,8,4,2,6,1,3,9,7]
	print(quick_sort(a, 0, len(a)-1))
