def sum_digits(number):
    lst = [x for x in str(number).replace('-', '')]
    a = 0
    for i in lst:
        a += int(i)
    return a