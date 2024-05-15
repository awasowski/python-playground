from datetime import datetime

i: int = 1000000000
j: int = 1
f: float = 10123.141592653589793

# number formatting
print(f"i: {i:_}")
print(f"f: {f:.2f}")
print(f"f: {f:.0f}")
print(f"f: {f:_.2f}")

# text aligning
text = "Hello World"
print(f"{text:_>20}:")
print(f"{text:-<20}:")
print(f"{text:=^20}:")

# print operation
print(f"{i + j = }")
print(f"{int(i - f) = }")

nums = [1, 2, 3, 4, 5]
print(f"{nums = }")
print(f"{list(map(lambda x: x * 2, nums)) = }")

def call_me(bool):
    return "I am true" if bool else "I am false"
print(f"{call_me(True) = }")

# date formatting
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
print(f"{now:%A, %B %d, %Y}")
print(f"local: {now:%c}")