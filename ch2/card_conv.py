def card_conv(x:int, r:int) -> str:
    d = ''
    d_char = '0123456789ABCDEFGHIJKLMONPQRSTUVWXYZ'
    
    while x > 0:
        d += d_char[x%r]
        x //= r
    return d[::-1]

if __name__ == "__main__":
    print(card_conv(4768,16))
    print(card_conv(2758,8))
