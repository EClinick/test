def inefficient_function(data):
    return sorted(set(data))


def slow_sum(numbers):
    return sum(numbers)


def slow_multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
