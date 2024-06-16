# You can use Protocol to define a callable class with a specific method signature.
from typing import Protocol

class Formatter(Protocol):
    def __call__(self, value: int) -> str:
        pass

def apply_formatter(formatter: Formatter, value: int) -> str:
    return formatter(value)

class IntToStrFormatter:
    def __call__(self, value: int) -> str:
        return f"Formatted number: {value}"

class TestClass:
    pass


formatter = IntToStrFormatter()
print(apply_formatter(formatter, 123))  # Output: "Formatted number: 123"
# mypy: "apply_formatter" has incompatible type "TestClass"; expected "Formatter"
# print(apply_formatter(TestClass(), 123))
