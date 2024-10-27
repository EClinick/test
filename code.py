def inefficient_function(data):
    """Return a list of unique elements from data."""
    return list(dict.fromkeys(data))


def slow_sum(numbers):
    """Return the sum of all elements in the iterable."""
    return sum(num for num in numbers)


def slow_multiply(numbers):
    if not numbers:
        raise ValueError('Input list is empty')
    product = 1
    for num in numbers:
        product *= num
    return product
