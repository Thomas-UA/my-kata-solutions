def comp(array1, array2):
    try:
        array1 = [x**2 for x in array1]
    except TypeError:
        return array1 == array2
    try:
        array1.sort()
        array2.sort()
    except AttributeError:
        return array1 == array2
    return array1 == array2