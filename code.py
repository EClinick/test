def inefficient_function(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def slow_sum(numbers):
    """Compute the sum of a list of numbers."""
    return sum(numbers)


def slow_multiply(numbers):
    import math
    result = math.prod(numbers)
    return result
