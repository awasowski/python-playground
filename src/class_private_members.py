class MyClass:
    def __init__(self, value):
        self.__private_field = value  # Private field

    def __private_method(self):
        print(f"This is a private method. Private field value: {self.__private_field}")

    def public_method(self):
        # Public method to access the private method
        self.__private_method()


# Creating an instance of MyClass
obj = MyClass("Private Value")

# Attempting to access the private field directly
try:
    print(obj.__private_field)
except AttributeError as e:
    # Output: Exception: 'MyClass' object has no attribute '__private_field'
    print(f"Exception: {e}")

# Attempting to access the private method directly
try:
    obj.__private_method()
except AttributeError as e:
    # Output: Exception: 'MyClass' object has no attribute '__private_method'
    print(f"Exception: {e}")

# Accessing the private method via a public method
obj.public_method()  # Output: This is a private method. Private field value: Private Value

# Accessing the private field via a mangled name (not recommended)
print(obj._MyClass__private_field)  # Output: Private Value
