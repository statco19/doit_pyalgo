# Boyer-Moore string matching algorithm

def bm_match(txt, pat) -> int:
	skip = [None] * 256
	N = len(txt)
	n = len(pat)
	
	# skip table
	for pt in range(256):
		skip[pt] = n
	
	for pt in range(n):
		skip[ord(pat[pt])] = n - pt - 1
		
	# string matching
	while pt < N:
		pp = n - 1
		while txt[pt] == pat[pp]:
			if pp == 0:
				return pt
			pt -= 1
			pp -= 1
		pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > (n - pp) else n - pp
		
	return -1

if __name__=="__main__": 
	s1 = "ABABCDEFGHA"
	s2 = "ABC"
	
	idx = bm_match(s1,s2)
	
	if idx == -1:
		print("doesn't exist.")
	else:
		print(idx)
