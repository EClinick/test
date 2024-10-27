def inefficient_function(data):
    """Return a list of unique elements from data."""
    return list(dict.fromkeys(data))


def slow_sum(numbers):
    return op.iadd(0, numbers)


def slow_multiply(numbers):
    if not numbers:
        raise ValueError('Input list is empty')
    return sum(numbers) if len(numbers) == 1 else math.prod(numbers)
