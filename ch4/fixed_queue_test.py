from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum("Menu", ["enque","deque","peek","find","dump","quit"])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
            
q = FixedQueue(64)

while True:
    print(f'The number of data: {len(q)} / {q.capacity}')
    menu = select_menu()
    
    if menu == Menu.enque:
        x = int(input('Enter the data: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('The queue is full.')
    
    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'The dequed data are {x}.')
        except FixedQueue.Empty:
            print('The queue is empty.')
            
    elif menu == Menu.peek:
        try:
            x = q.peek()
            print(f'The peeked data are {x}.')
        except FixedQueue.Empty:
            print('The queue is empty.')
     
    elif menu == Menu.find:
        x = int(input("Enter the data: "))
        if x in q:
            print(f'The queue has {q.count(x)} data, the indice of the first datum is {q.find(x)}.')
        else:
            print("Cannot find the data.")
                
    elif menu == Menu.dump:
        q.dump()
        
    else:
        break
