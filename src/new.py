class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Example(Singleton):
    def __new__(cls, *args, **kwargs):
        print("Creating instance in __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Initializing instance in __init__")
        self.value = value


# Create an instance of Example
example = Example(42)
example2 = Example(11)

print(example is example2)
