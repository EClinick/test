def inefficient_function(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result
