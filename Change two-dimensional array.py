def matrix(array):
    a=0
    for i in array:
        if i[a] < 0:
            i[a]=0
            a+=1
        elif i[a] >= 0:
            i[a]=1
            a+=1
    return array