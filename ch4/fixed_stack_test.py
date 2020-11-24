from enum import Enum
from fixed_stack import FixedStack

Menu = Enum("Menu",['push','pop','peek','find','dump','quit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            
            return Menu(n)
            
s = FixedStack(64)

while True:
    print(f'The number of data: {len(s)} / {s.capacity}')
    menu = select_menu()
    
    if menu == Menu.push:
        x = int(input('Enter data: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print("The stack is full.")
    
    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'The popped datum is {x}.')
        except FixedStack.Empty:
            print("The stack is empty.")
            
    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f'The peeked data are {x}.')
        except FixedStack.Empty:
            print("The stack is empty.")
            
    elif menu == Menu.find:
        x = int(input("Enter data to find: "))
        if x in s:
            print(f"The stack has found {s.count(x)} data(datum), its head's indice is {s.find(x)}.")
        else:
            print("Cannot find the data")
            
    elif menu == Menu.dump:
        s.dump()
        
    else:
        break
