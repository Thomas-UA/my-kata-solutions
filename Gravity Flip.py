def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)

assert flip('R', [3, 2, 1, 2]) == [1, 2, 2, 3]
assert flip('L', [1, 4, 5, 3, 5]) == [5, 5, 4, 3, 1]
