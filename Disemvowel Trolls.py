def disemvowel(string_):
    x = 'AaEeUuIiOo'
    for i in x:
        string_ = string_.replace(i, '')
    return string_