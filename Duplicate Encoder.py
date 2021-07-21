def duplicate_encode(word):
    s = ''
    for i in word:
        if i.isalpha():
            if i.isupper():
                if word.count(i) + word.count(i.lower()) != 1: 
                     s += ')'
                else:
                     s += '('
            else:
                if word.count(i) + word.count(i.upper()) != 1: 
                    s += ')'
                else:
                    s += '('
        else:
            if word.count(i) != 1:
                s += ')'
            else:
                s += '('
    return s