def factorial(n):
    o = 1
    if n == 0:
        return 1
    if (n > 0) and (n < 13):
        for i in range(1, n + 1):
            o = o * i
        return o
    else:
        raise ValueError