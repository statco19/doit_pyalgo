# getting median 1

def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        if c >= a:
            return a
        else:
            return c
    elif a > c:
        return a
    elif c > b:
        return b
    else:
        return c
a = int(input("type a number: "))
b = int(input("type a number: "))
c = int(input("type a number: "))

print(f"the median is {med3(a,b,c)}")
