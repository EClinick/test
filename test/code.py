def inefficient_function(data):
    seen = set()
    result = []
    for value in data:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return tuple(sorted(result))


def slow_sum(numbers):
    return sum(numbers)


def slow_multiply(numbers):
    product = 1 if numbers else None
    for num in numbers:
        product *= num
    return product
