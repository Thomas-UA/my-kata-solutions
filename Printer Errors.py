def printer_error(s):
    bad_color = 'nopqrstuvwxyz'
    count = 0
    for symbol in s:
        if symbol in bad_color: count += 1
    
    return f"{count}/{len(s)}"