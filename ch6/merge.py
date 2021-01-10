from typing import Sequence, MutableSequence
import heapq

def merge_sorted_list(a: Sequence,b: Sequence, c: MutableSequence):
	pa, pb, pc = 0, 0, 0
	
	na, nb, nc = len(a), len(b), len(c)
	
	while pa<na and pb<nb:
		if a[pa] <= b[pb]:
			c[pc] = a[pa]
			pa += 1
		else:
			c[pc] = b[pb]
			pb += 1
		
		pc += 1
		
	while pa < na:
		c[pc] = a[pa]
		pa += 1
		pc += 1
		
	while pb < nb:
		c[pc] = b[pb]
		pb += 1
		pc += 1
		
	return c
	
if __name__ == "__main__":
	a = [2,4,6,8,11,13]
	b = [1,2,3,4,9,16,12]
	c = [None] * len(a+b)
	
	print(merge_sorted_list(a,b,c))
	print(list(heapq.merge(a,b)))
