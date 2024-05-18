# Higher order functions

# Function as an argument
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x


result = apply_function(square, 5)  # Output: 25
print(result)

# Function as a return value
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
