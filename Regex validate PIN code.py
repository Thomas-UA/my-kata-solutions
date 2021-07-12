def validate_pin(pin):
    s = 0
    for i in pin:
        if i in ("0123456789"):
            s += 1
    if len(pin) == 6:
        if s == len(pin):
            return True
        else:
            return False
    if len(pin) == 4:
        if s == len(pin):
            return True
        else:
            return False
    else:
        return False