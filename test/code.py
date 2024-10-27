def inefficient_function(data: Iterable[str]) ->Tuple[str, ...]:
    unique_data = set(data)
    sorted_data = tuple(sorted(unique_data))
    return sorted_data


def slow_sum(numbers):
    return sum(numbers)


def slow_multiply(numbers: list[int]) ->(int | None):
    if not all(isinstance(num, int) for num in numbers):
        return None
    result = 1
    for num in numbers:
        result *= num
    return result
