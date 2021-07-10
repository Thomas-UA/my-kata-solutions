def high_and_low(numbers):
    x = [int(s) for s in numbers.split(' ')]
    return str(max(x)) + " " + str(min(x))