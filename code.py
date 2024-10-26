def inefficient_function(data):
    seen = set()
    result = [item for item in data if not (item in seen or seen.add(item))]
    return result
