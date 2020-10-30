from typing import Sequence, Any
import copy

def seq_search(seq: Sequence, key:Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)
    
    i=0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i==len(seq) else i
    
if __name__ == "__main__":
    num = int(input("The number of elements: "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input("What to search?: "))
    idx = seq_search(x,ky)
    
    if idx == -1:
        print("No such an element.")
    else:
        print(f'The element is at x[{idx}]')
