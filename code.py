def inefficient_function(data):
    return list(dict.fromkeys(data))


def slow_sum(numbers):
    if not numbers:
        return 0
    result = 0
    for num in numbers:
        result += num
    return result


def slow_multiply(numbers):
    if not numbers:
        raise ValueError('Input list is empty')
    return 1 if len(numbers) == 1 else prod(numbers)
