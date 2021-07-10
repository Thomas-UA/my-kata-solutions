def tickets(people):
    k = []
    for i in people:
        if i == 25:
            k.append(i)
        elif i == 50:
            k.append(i)
            try:
                k.remove(25)
            except ValueError:
                return 'NO'
        elif i == 100:
            k.append(i)
            try:
                k.remove(50)
            except ValueError:
                try:
                    k.remove(25)
                    k.remove(25)
                except ValueError:
                    return 'NO'
                else:
                    try:
                        k.remove(25)
                    except ValueError:
                        return 'NO'
            else:
                try:
                    k.remove(25)
                except ValueError:
                    return 'NO'
    return 'YES'