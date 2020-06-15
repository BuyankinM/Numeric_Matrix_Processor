def multiply(a, b):
    if b == 0:  # base case
        return 0
    # recursive case
    return a + multiply(a, b - 1)