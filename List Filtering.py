def filter_list(l):
    o = []
    for i in l:
        try:
            i + "a"
        except TypeError:
            o.append(i)
        else:
            pass
    return o