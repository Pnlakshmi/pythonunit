import unittest
from calculator import Calculator


class TestCalculatorAdd(unittest.TestCase):
    """Tests for the add method."""

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_add_mixed_sign(self):
        self.assertEqual(self.calc.add(-1, 5), 4)

    def test_add_zeros(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)


class TestCalculatorSubtract(unittest.TestCase):
    """Tests for the subtract method."""

    def setUp(self):
        self.calc = Calculator()

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtract_zeros(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)


class TestCalculatorMultiply(unittest.TestCase):
    """Tests for the multiply method."""

    def setUp(self):
        self.calc = Calculator()

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_mixed_sign(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)


class TestCalculatorDivide(unittest.TestCase):
    """Tests for the divide method."""

    def setUp(self):
        self.calc = Calculator()

    def test_divide_evenly(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_with_remainder(self):
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333, places=3)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))


class TestCalculatorPower(unittest.TestCase):
    """Tests for the power method."""

    def setUp(self):
        self.calc = Calculator()

    def test_power_positive(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_power_one_exponent(self):
        self.assertEqual(self.calc.power(7, 1), 7)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(self.calc.power(2, -1), 0.5)


class TestCalculatorModulo(unittest.TestCase):
    """Tests for the modulo method."""

    def setUp(self):
        self.calc = Calculator()

    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

    def test_modulo_by_zero_raises(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)


class TestCalculatorAverage(unittest.TestCase):
    """Tests for the average method."""

    def setUp(self):
        self.calc = Calculator()

    def test_average_basic(self):
        self.assertEqual(self.calc.average([2, 4, 6]), 4)

    def test_average_single_element(self):
        self.assertEqual(self.calc.average([5]), 5)

    def test_average_with_negatives(self):
        self.assertEqual(self.calc.average([-2, 2]), 0)

    def test_average_empty_list_raises(self):
        with self.assertRaises(ValueError):
            self.calc.average([])


class TestCalculatorFactorial(unittest.TestCase):
    """Tests for the factorial method."""

    def setUp(self):
        self.calc = Calculator()

    def test_factorial_zero(self):
        self.assertEqual(self.calc.factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(self.calc.factorial(1), 1)

    def test_factorial_five(self):
        self.assertEqual(self.calc.factorial(5), 120)

    def test_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    def test_factorial_float_raises(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(3.5)


class TestCalculatorAddExtended(unittest.TestCase):
    """Extended tests for the add method."""

    def setUp(self):
        self.calc = Calculator()

    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_add_float_and_integer(self):
        self.assertAlmostEqual(self.calc.add(1.5, 2), 3.5)


class TestCalculatorSubtractExtended(unittest.TestCase):
    """Extended tests for the subtract method."""

    def setUp(self):
        self.calc = Calculator()

    def test_subtract_from_itself(self):
        self.assertEqual(self.calc.subtract(42, 42), 0)

    def test_subtract_large_numbers(self):
        self.assertEqual(self.calc.subtract(1000000, 999999), 1)


class TestCalculatorDivideExtended(unittest.TestCase):
    """Extended tests for the divide method."""

    def setUp(self):
        self.calc = Calculator()

    def test_divide_one_by_one(self):
        self.assertEqual(self.calc.divide(1, 1), 1)

    def test_divide_returns_float(self):
        self.assertIsInstance(self.calc.divide(5, 2), float)


class TestCalculatorMultiplyExtended(unittest.TestCase):
    """Extended tests for the multiply method."""

    def setUp(self):
        self.calc = Calculator()

    def test_multiply_by_one(self):
        self.assertEqual(self.calc.multiply(99, 1), 99)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)


class TestCalculatorFactorialExtended(unittest.TestCase):
    """Extended tests for the factorial method."""

    def setUp(self):
        self.calc = Calculator()

    def test_factorial_ten(self):
        self.assertEqual(self.calc.factorial(10), 3628800)

    def test_factorial_returns_integer(self):
        self.assertIsInstance(self.calc.factorial(5), int)


if __name__ == "__main__":
    unittest.main()
