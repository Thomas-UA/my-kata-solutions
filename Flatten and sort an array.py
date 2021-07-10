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

flatten_and_sort([])
flatten_and_sort([[], []])
flatten_and_sort([[], [1]])
flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])
flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])