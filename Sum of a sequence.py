def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    elif begin_number == end_number:
        return begin_number
    elif begin_number < end_number:
        return sum(range(begin_number, end_number + 1, step))