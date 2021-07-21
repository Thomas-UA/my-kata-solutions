def revrot(strng, sz):
    if len(strng) < sz or sz <= 0 or strng == '':
        return ''
    else:
        s = ''
        y = 0
        for i in range(int(len(strng)/sz)):
            y += sz
            x = y - sz
            try:
                k = strng[x:y]
            except IndexError:
                break
            else:
                a = 0
                for l in k:
                    a += int(l)**3
                if a % 2 == 0:
                    k = k[::-1]
                else:
                    k = k[1::1] + k[0]
            s += k
        return s