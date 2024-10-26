def inefficient_function(data):
    return sorted(set(data))


def slow_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def slow_multiply(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
