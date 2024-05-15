from functools import reduce
import operator


def add3(a, b, c):
    return a + b + c


print("* operator: Unpacks an iterable (like list, tuple, etc.) into positional arguments:")
print(1, 2, 3)
print([1, 2, 3])
print(*[1, 2, 3])  # unpack during call

print(f"{add3(1, 2, 3)=}")
print(f"{add3(*[1, 2, 3])=}")

print("\nAs a function argument, * operator packs positional arguments into a tuple:")


def add(*args):
    print(f"{args=}")
    return sum(args)


print(f"{add(1, 2, 3)=}")
print(f"{add(*[1, 2, 3])=}")

print("\n** operator: Unpacks a dictionary into keyword arguments:")


def sub3(a=0, b=0, c=0):
    return a - b - c


print(f"{sub3(**{'a': 1, 'b': 2, 'c': 3})=}")
print(f"{sub3(a=1, b=2, c=3)=}")

print("\nAs a function argument, ** operator packs keyword arguments into a dictionary:")


def sub(**kwargs):
    print(f"{kwargs=}")
    return reduce(operator.sub, kwargs.values())


print(f"{sub(a=1, b=2, c=3)=}")
