# Functional Programming in Python

# Map
from functools import reduce
def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


# Filter
def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]


# Reduce
def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]
sum = reduce(add, numbers)
print(sum)  # Output: 15