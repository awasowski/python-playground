# A closure is a function that retains access to its lexical scope,
# even when the function is executed outside that scope.

# Closures are often used to create factory functions.
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


# Create a closure
closure = outer_function("Hello, World!")
closure2 = outer_function("Hello, Python!")

# Call the closure
closure()
closure2()

# Timer example
def make_counter():
    count = 0

    def counter():
        nonlocal count  # Refers to the 'count' variable in the enclosing scope
        count += 1
        return count

    return counter


# Create a counter closure
counter1 = make_counter()
# Each call to make_counter() creates a new closure, capturing a unique count variable.
counter2 = make_counter()

# Use the counters
print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1
print(counter2())  # Output: 2
