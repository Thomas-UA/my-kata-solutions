morse = {'.-':'A','-...':'B','-.-.':'C','-..':'D',
    '.':'E','..-.':'F','--.':'G','....':'H','..':'I',
    '.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N',
    '---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S',
    '-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z','.----.':'-', '----':' ', ' ':' ', '...---...': 'SOS', '-.-.--':'!', '.-.-.-':'.'}

def decodeMorse(morse_code):
    output_string = ''
    symbols = ''

    if morse_code[0] == ' ':
        morse_code = morse_code.lstrip()

    if len(morse_code) > 0:
        morse_code = morse_code + ' '
    else:
        return ''
    
    for i in morse_code:
        if i != ' ':
            symbols += i
        elif len(symbols) != 0:
            output_string += str(morse.get(symbols))
            symbols = ''
        elif i == ' ' and len(symbols) == 0:
            symbols += ' '
        
    return output_string.rstrip()