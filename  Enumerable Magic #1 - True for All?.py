def all(seq, fun):
    return next((False for x in seq if not fun(x)), True)