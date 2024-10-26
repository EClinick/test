def inefficient_function(data):
    return list(dict.fromkeys(data))


def slow_sum(numbers):
    return sum(numbers)


def slow_multiply(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
