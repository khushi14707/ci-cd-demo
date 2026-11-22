class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


if __name__ == "__main__":
    calc = Calculator()
    print("5 + 3 =", calc.add(5, 3))
    print("5 - 3 =", calc.subtract(5, 3))