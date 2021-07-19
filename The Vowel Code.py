enc = {
    'a':'1',
    'e':'2',
    'i':'3',
    'o':'4',
    'u':'5'
}

dec = {
    '1':'a',
    '2':'e',
    '3':'i',
    '4':'o',
    '5':'u'
}

def encode(st):
    x = list(st)
    s = ''
    for i in range(0, len(x)):
        w = x[i]
        if w in enc.keys():
            x[i] = enc[w]
    for i in x:
        s += i
    return s

    
def decode(st):
    x = list(st)
    s = ''
    for i in range(0, len(x)):
        w = x[i]
        if w in dec.keys():
            x[i] = dec[w]
    for i in x:
        s += i
    return s

