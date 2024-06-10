class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Negative balance not allowed")
        self._balance = amount

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    acc = Account(100)
    print(f"Current balance is: {acc.balance}")
    try:
        acc.balance -= 150
    except ValueError as e:
        print(e)
    print(f"Current balance is: {acc.balance}")

    rect = Rectangle(10, 20)
    print(f"Area of rectangle is: {rect.area}")
    rect.width = 100
    print(f"Area of rectangle is: {rect.area}")