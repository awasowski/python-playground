from typing import List

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

# bad type: return type should be int, not str
def sum_list(numbers: List[int]) -> int:
    return str(sum(numbers))

# mypy won't yell at this function
def sum_list_without_hints(numbers):
    return sum(numbers)

if __name__ == "__main__":
    print(greet("World"))
    print(add_numbers(5, 7))
    print(sum_list([1, 2, 3, 4, 5]))
