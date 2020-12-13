# 8 queen problem

pos = [0] * 8				# Queens' positions in columns
flag_row = [False] * 8	# check if Queens are in rows
flag_left_diagonals = [False] * 15
flag_right_diagonals = [False] * 15

def put() -> None:
	for j in range(8):		# j means rows
		for i in range(8):	# i means columns
			print('Q' if pos[i] == j else 'X', end='')
		print()
	print()
	
def set(i:int) -> None:
	for j in range(8):
		if (not flag_row[j] and not flag_left_diagonals[i+j] and not flag_right_diagonals[i-j+7]):
			pos[i] = j
		
			if i == 7:
				put()
			else:
				flag_row[j] = flag_left_diagonals[i+j] = flag_right_diagonals[i-j+7] = True
				
				set(i+1)
				
				flag_row[j] = flag_left_diagonals[i+j] = flag_right_diagonals[i-j+7] = False
			
if __name__ == "__main__":
	set(0)
