def inefficient_function(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


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
