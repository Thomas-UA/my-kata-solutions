def countBits(n):
    x = ''
    for i in bin(n):
        x = x + x.join(str(i))
    return x.count('1')