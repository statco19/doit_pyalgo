n = int(input("How many integer would you like to store?: "))
a = [None] * n

cnt = 0
while True:
    a[cnt%n] = int(input(f'Enter integer no.{cnt + 1}: '))
    cnt += 1
    
    retry = input(f"continue?(Y ... Yes / N ... No): ")
    if retry in {'N', 'n'}:
        break
        
i = cnt - n
if i<0: i=0

while i<cnt:
    print(f'integer no.{i+1} = {a[i%n]}')
    i += 1
