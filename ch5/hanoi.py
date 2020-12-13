#towers of Hanoi
"""
def move(n:int, x:int, y:int) -> None:
	
	if n > 1:
		move(n-1, x, 6-x-y)
	
	print(f'Group [{n}] was moved from {x} to {y}.')
	
	if n > 1:
		move(n-1, 6-x-y, y)
"""
n = int(input())
cnt = 0

def moveCnt(n,x=1,y=3):
    global cnt
    if n > 1:
        moveCnt(n-1,x,6-x-y)
        
    cnt += 1
    
    if n > 1:
        moveCnt(n-1,6-x-y,y)

def move(n,x=1,y=3):
    if n > 1:
        move(n-1,x,6-x-y)

    print(f'{x} {y}')

    if n > 1:
        move(n-1,6-x-y,y)

moveCnt(n,1,3)
print(cnt)
move(n,1,3)
