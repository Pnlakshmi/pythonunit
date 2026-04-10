class Calculator:
    """A simple calculator with basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        return a % b

    def average(self, numbers):
        if not numbers:
            raise ValueError("Cannot compute average of empty list")
        return sum(numbers) / len(numbers)

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial requires a non-negative integer")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
