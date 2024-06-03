class MyClass:
    # Class variable
    value = "Class Level"

    def __init__(self, value):
        # Instance variable
        self.value = value


# Creating instances of MyClass
obj1 = MyClass("Instance Level 1")
obj2 = MyClass("Instance Level 2")

# Accessing variables
print(MyClass.value)    # Output: Class Level
print(obj1.value)       # Output: Instance Level 1
print(obj2.value)       # Output: Instance Level 2

# Modifying the class variable
MyClass.value = "New Class Level"

print(MyClass.value)    # Output: New Class Level
print(obj1.value)       # Output: Instance Level 1
print(obj2.value)       # Output: Instance Level 2

# Modifying the instance variable
obj1.value = "Modified Instance Level 1"

print(MyClass.value)    # Output: New Class Level
print(obj1.value)       # Output: Modified Instance Level 1
print(obj2.value)       # Output: Instance Level 2
