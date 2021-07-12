def dig_pow(n, p):
    result = 0
    for i in str(n):
        result += pow(int(i), p)
        p += 1
    if result%n != 0:
        return -1
    else:
        return int(result/n)