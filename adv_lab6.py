
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = []
        for i in range(self.rows):
            row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)

class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return CustomString(self.value + other.value)

    def __mul__(self, times):
        return CustomString(self.value * times)

    def to_upper(self):
        return self.value.upper()

    def __str__(self):
        return self.value

class Currency:
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'INR': 74.5
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add amounts with different currencies")
        return Currency(self.amount + other.amount, self.currency)

    def convert_to(self, new_currency):
        if new_currency not in Currency.exchange_rates:
            raise ValueError("Unsupported currency")
        usd_amount = self.amount / Currency.exchange_rates[self.currency]
        new_amount = usd_amount * Currency.exchange_rates[new_currency]
        return Currency(new_amount, new_currency)

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __lt__(self, other):
        return self.width < other.width

    def __eq__(self, other):
        return self.width == other.width

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

if __name__ == "__main__":
    print("=== Matrix Addition ===")
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print(m1 + m2)

    print("\n=== Custom String ===")
    s1 = CustomString("Hello")
    s2 = CustomString("World")
    print(s1 + s2)
    print(s1 * 3)
    print(s1.to_upper())

    print("\n=== Currency Conversion ===")
    c1 = Currency(100, 'USD')
    c2 = Currency(50, 'USD')
    print(c1 + c2)
    print(c1.convert_to('INR'))

    print("\n=== Rectangle Comparison ===")
    r1 = Rectangle(10, 5)
    r2 = Rectangle(15, 5)
    print(f"{r1} < {r2}: {r1 < r2}")
    print(f"{r1} == {r2}: {r1 == r2}")
