def count_positives_sum_negatives(arr):
    return [] if len(arr) == 0 else [len([x for x in arr if x > 0]), [sum(x for x in arr if x < 0)][0]]