def flatten_and_sort(array):
    array = str(array).split()
    x = []
    for i in array:
        i = i.replace('"', '')
        i = i.replace('[', '')
        i = i.replace(']', '')
        i = i.replace(',', '')
        try:
            x.append(int(i))
        except ValueError:
            pass
    x.sort()
    return x