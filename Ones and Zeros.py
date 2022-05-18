def binary_array_to_number(arr):
    v = [str(x) for x in arr]
    s = ''.join(v)
    return int(s, 2)