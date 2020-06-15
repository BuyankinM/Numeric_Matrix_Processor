def last_indexof_max(numbers):
    if not numbers:
        return -1
    ind = 0

    for i, num in enumerate(numbers[1:], 1):
        if num >= numbers[ind]:
            ind = i

    return ind