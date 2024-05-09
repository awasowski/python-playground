# A metaclass in Python is a class of a class. It defines how classes behave.
# Just as classes are blueprints for creating objects,
# metaclasses are blueprints for creating classes themselves.

# Create a metaclass that validates attributes and methods
class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_method' not in dct:
            raise TypeError(f"{name} must have a 'required_method'")
        return super().__new__(cls, name, bases, dct)

# Class using the metaclass


class ValidatedClass(metaclass=ValidateMeta):
    def required_method(self):
        return "This method is required!"


# This will raise an error because it lacks the required method
try:
    class InvalidClass(metaclass=ValidateMeta):
        pass
except TypeError as e:
    print(e)  # Outputs: InvalidClass must have a 'required_method'
