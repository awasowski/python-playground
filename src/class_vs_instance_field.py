class MyClass:
    # This is a class variable
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        # This is an instance variable
        self.instance_variable = instance_variable


# Create two instances of MyClass
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

# Access the class variable
print(MyClass.class_variable)  # Output: I am a class variable
print(obj1.class_variable)     # Output: I am a class variable
print(obj2.class_variable)     # Output: I am a class variable

# Access the instance variables
print(obj1.instance_variable)  # Output: Instance 1
print(obj2.instance_variable)  # Output: Instance 2

# Modify the class variable
MyClass.class_variable = "New class variable value"

print(MyClass.class_variable)  # Output: New class variable value
print(obj1.class_variable)     # Output: New class variable value
print(obj2.class_variable)     # Output: New class variable value

# Modify an instance variable
obj1.instance_variable = "Modified Instance 1"

print(obj1.instance_variable)  # Output: Modified Instance 1
print(obj2.instance_variable)  # Output: Instance 2
