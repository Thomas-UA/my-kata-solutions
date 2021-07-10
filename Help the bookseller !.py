def stock_list(listOfArt, listOfCat):
    calculate = {}
    for i in listOfArt:
        a = ''
        ia = 0
        if i[0] in listOfCat:
            if i[0] in calculate:
                pass
            else:
                calculate[i[0]] = 0
            for l in range(0, len(i)):
                try:
                    int(i[l])
                except ValueError:
                    pass
                else:
                    a = a + i[l]
            ia = int(a)
            calculate[i[0]] = int(calculate[i[0]]) + ia
    o = ''
    for k in range(0, len(listOfCat)):
        try:
            s = calculate[listOfCat[k]]
        except KeyError:
            o = o + ("(" + listOfCat[k] + " : 0) - ")
        else:
            o = o + ("(" + listOfCat[k] + " : " + str(s) + ")" + " - ")
    d = len(o) - 3
    if all(x == 0 for x in calculate.values()):
        return ''
    return o[:d]