from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
    
if __name__ == "__main__":
    print("Getting the maximum value of an array.")
    num = int(input("Enter the number of elements: "))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f"Enter the value of x[{i}]: "))
        
    print(f"The maximum value is {max_of(x)}.")
