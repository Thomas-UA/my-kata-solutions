def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1 if ((sq**0.5) - int(sq**0.5)) != 0 else ((sq**0.5) + 1)**2
