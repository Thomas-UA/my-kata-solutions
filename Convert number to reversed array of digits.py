def digitize(n):
    n = str(n)[::-1]
    return [int(x) for x in n]