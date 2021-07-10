def round_to_next5(n):
    return n if (n == 0) or (n % 5) == 0 else (n - (n % 5)) + 5
