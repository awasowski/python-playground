from typing import TypeVar, Generic, List

# Define a type variable
T = TypeVar('T')

# Create a generic class
class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items

# Example usage
stack_of_ints = Stack[int]()
stack_of_ints.push(1)
stack_of_ints.push(2)
print(stack_of_ints.pop())  # Output: 2
print(stack_of_ints.pop())  # Output: 1

stack_of_strings = Stack[str]()
stack_of_strings.push("hello")
stack_of_strings.push("world")
print(stack_of_strings.pop())  # Output: world
print(stack_of_strings.pop())  # Output: hello