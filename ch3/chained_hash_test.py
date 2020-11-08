from enum import Enum
from chained_hash import ChainedHash

Menu = Enum("Menu", ['add', 'remove', 'search', 'dump', 'quit'])

def select_menu() -> Menu:
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)
            
hash = ChainedHash(13) # constructing a hash table with the size of 13

while True:
    menu = select_menu()
    
    if menu == Menu.add:
        key = int(input("Enter a key to add: "))
        val = input("Enter a value to add: ")
        if not hash.add(key, val):
            print("Addition failed")
    
    elif menu == Menu.remove:
        key = int(input("Enter a key to remove: " ))
        if not hash.remove(key):
            print("Remove failed.")
            
    elif menu == Menu.search:
        key = int(input("Enter a key to search: "))
        t = hash.search(key)
        if t is not None:
            print(f'The value of the key is {t}.')
        else:
            print("No such data.")
    
    elif menu == Menu.dump:
        hash.dump()
        
    else:
        break
