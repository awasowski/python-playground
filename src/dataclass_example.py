from dataclasses import dataclass

@dataclass
class Person:
    name: str = "Unknown"
    age: int = 0


# Creating instances of Person
person1 = Person()  # Uses default values
person2 = Person("Alice", 30)  # Overrides default values

# Each instance has its own instance variables
print(person1)  # Output: Person(name='Unknown', age=0)
print(person2)  # Output: Person(name='Alice', age=30)

# Accessing instance variables
print(person1.name)  # Output: Unknown
print(person2.age)   # Output: 30

# Modifying instance variables
person1.name = "Bob"
person1.age = 25
print(person1)  # Output: Person(name='Bob', age=25)
