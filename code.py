# code.py

def inefficient_function(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

def slow_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def slow_multiply(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
