def two_sort(array):
    s = ''
    t = sorted(array)
    for i in range(0, len(t[0])):
        s += t[0][i] + '***'
    return s[0:len(s)-3]