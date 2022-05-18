def persistence(n):
    num_of_tries = 0

    if len(str(n)) == 1:

        return num_of_tries

    elif '0' in str(n):

        return 1

    list_with_numbers = [int(x) for x in str(n)]

    while len(list_with_numbers) > 1:
        return_value = list_with_numbers.pop(0)
        for _ in range(len(list_with_numbers)):
            return_value *= list_with_numbers[_]

        num_of_tries += 1

        list_with_numbers = [int(x) for x in str(return_value)]

    else:
        return num_of_tries