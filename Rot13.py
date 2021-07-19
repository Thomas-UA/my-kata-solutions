def rot13(message):
    l = 'abcdefghijklmnopqrstuvwxyz'
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v = ',./*-+0123456789!_ '
    o_s = ''
    for i in message:
        if i in v:
            o_s += o_s.join(i)
        elif i.islower():
            try:
                c = l[l.index(i) + 13]
                o_s += o_s.join(c)
            except IndexError:
                c = l[l.index(i) - 13]
                o_s += o_s.join(c)
        elif i.isupper():
            try:
                c = u[u.index(i) + 13]
                o_s += o_s.join(c)
            except IndexError:
                c = u[u.index(i) - 13]
                o_s += o_s.join(c)
    return o_s