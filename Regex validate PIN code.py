def validate_pin(pin):
    s = 0
    for i in pin:
        if i in ("0123456789"):
            s += 1
    if len(pin) == 4 or len(pin) == 6: return len(pin) == s
    else: return False