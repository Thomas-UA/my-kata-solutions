def sum_of_integers_in_string(s):
    s += ' '
    x = []
    a = ''
    for i in s:
        if i.isdigit():
            a += i
        elif len(a) > 0:
            x.append(int(a))
            a = ''
    return sum(x)