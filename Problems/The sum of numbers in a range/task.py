def range_sum(list_numbers, min_a, min_b):
    s = 0
    for num in list_numbers:
        if min_a <= num <= min_b:
            s += num
    return s


numbers = [int(num) for num in input().split()]
a, b = [int(num) for num in input().split()]
print(range_sum(numbers, a, b))
