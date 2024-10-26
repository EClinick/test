def inefficient_function(data):
    return sorted(set(data))


def slow_sum(numbers):
    if not numbers:
        raise ValueError('Input list cannot be empty')
    return sum(n for n in numbers)


def slow_multiply(numbers):
    import math
    return math.prod(numbers)
