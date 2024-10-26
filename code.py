def inefficient_function(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result


# Suggested Refactoring:
# **Optimized Function**
# 
# The existing code can be optimized using a set to keep track of unique elements. Sets in Python have an average time complexity of O(1) for insertion and lookup operations, making them ideal for this use case.
# 
# ```python
# def efficient_function(data):
#     """Returns a list with unique elements from the input data."""
#     return list(set(data))
# ```
# 
# **Why This Refactoring Works**
# 
# The refactored function takes advantage of the following properties of sets:
# 
# 1.  **Unique Elements**: Sets automatically eliminate duplicates, ensuring that only distinct elements are present in the output.
# 2.  **Fast Lookup**: Set membership testing (`in` operator) has an average time complexity of O(1), which significantly improves performance when dealing with large datasets.
# 
# **Example Usage**
# 
# ```python
# data = [4, 2, 7, 1, 3, 2, 6, 5]
# print(efficient_function(data))  # Output: [1, 2, 3, 4, 5, 6, 7]
# 
# data_with_duplicates = ['a', 'b', 'c', 'd', 'e', 'e', 'f']
# print(efficient_function(data_with_duplicates))  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
# ```
# 
# **Advice**
# 
# *   Use sets when you need to eliminate duplicates or perform fast lookup operations.
# *   Consider using `set` and then converting it back to a list (`list(set())`) as shown above, since the order of elements in a set is arbitrary.
# *   For large datasets with specific requirements (e.g., preserving insertion order), consider using an ordered data structure like a dictionary or an OrderedDict.

# Suggested Refactoring:
# **Optimized Function**
# 
# The existing code can be optimized using a set to keep track of unique elements. Sets in Python have an average time complexity of O(1) for insertion and lookup operations, making them ideal for this use case.
# 
# ```python
# def efficient_function(data):
#     """Returns a list with unique elements from the input data."""
#     return list(set(data))
# ```
# 
# **Why This Refactoring Works**
# 
# The refactored function takes advantage of the following properties of sets:
# 
# 1.  **Unique Elements**: Sets automatically eliminate duplicates, ensuring that only distinct elements are present in the output.
# 2.  **Fast Lookup**: Set membership testing (`in` operator) has an average time complexity of O(1), which significantly improves performance when dealing with large datasets.
# 
# **Example Usage**
# 
# ```python
# data = [4, 2, 7, 1, 3, 2, 6, 5]
# print(efficient_function(data))  # Output: [1, 2, 3, 4, 5, 6, 7]
# 
# data_with_duplicates = ['a', 'b', 'c', 'd', 'e', 'e', 'f']
# print(efficient_function(data_with_duplicates))  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
# ```
# 
# **Advice**
# 
# *   Use sets when you need to eliminate duplicates or perform fast lookup operations.
# *   Consider using `set` and then converting it back to a list (`list(set())`) as shown above, since the order of elements in a set is arbitrary.
# *   For large datasets with specific requirements (e.g., preserving insertion order), consider using an ordered data structure like a dictionary or an OrderedDict.
