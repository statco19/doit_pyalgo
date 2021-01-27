def bf_match(txt, pat) -> int:
	pt = 0
	pp = 0
	
	while pt != len(txt) and pp != len(pat):
		if txt[pt] == pat[pp]:
			pt += 1
			pp += 1
			
		else:
			pt = pt-pp + 1
			pp = 0
			
	return pt-pp if pp == len(pat) else -1

if __name__=="__main__": 
	txt = "ABABCDEFGHA"
	pat = "ABC"
	print(bf_match(txt, pat))
	
	assert(pat in txt)
	print(True)
	
	print(txt.find(pat))
	print(txt.rfind(pat))
	print(txt.index(pat))
	print(txt.rindex(pat))
	print(txt.startswith(pat))
	print(txt.endswith(pat))
	
