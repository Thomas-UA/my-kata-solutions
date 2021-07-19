def increment_string(strng):
    strng = strng[::-1]
    s_l = ''
    i_l = ''
    c = 0
    for i in strng:
        try:
            int(i)
        except ValueError:
            c = strng.find(i)
            break
        else:
            i_l += i_l.join(i)
    if c != 0:
        for i in strng[c:]:
            s_l += s_l.join(i)
    else:
        try:
            int(strng)
        except ValueError:
            s_l = strng
        else:
            s_l = ''
    k = len(i_l)
    if k == 0:
        i_l = '1'
        i_l = int(i_l)
    else:
        i_l = i_l[::-1]
        i_l = int(i_l)
        i_l += 1
        if len(str(i_l)) < k:
            i_l = str(i_l)
            i_l = i_l[::-1]
            while len(i_l) < k:
                i_l += '0'
        else:
            i_l = str(i_l)
            i_l = i_l[::-1]
    i_l = str(i_l)
    return s_l[::-1] + i_l[::-1]

    '''
Below the good code from somebody, his/her code is good 👍
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
    '''