from functools import partial

# Higher-order function that takes a function and a list
def map_function(func, items):
    return [func(item) for item in items]

# Currying example using functools.partial
def multiply(x, y):
    return x * y


# Create a new function that multiplies by 2
multiply_by_2 = partial(multiply, 2)

# Use the higher-order function with the curried function
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map_function(multiply_by_2, numbers)

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

multiply_by_3 = partial(multiply, 3)
tripled_numbers = map(multiply_by_3, numbers)  # map is a built-in higher-order function

print(list(tripled_numbers))  # Output: [3, 6, 9, 12, 15]
