def find_it(seq):
    a = 0
    for i in seq:
        a = seq.count(i)
        if a % 2 != 0:
            return i