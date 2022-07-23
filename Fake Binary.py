def fake_bin(x):
    string = ''
    for number in x:
        if int(number) < 5:
            string+='0'
        else:
            string+='1'
    return string