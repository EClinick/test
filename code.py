def inefficient_function(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def slow_sum(numbers):
    return sum(numbers)


def slow_multiply(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
