import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(4, 2) == 8

    def test_division_success(self):
        assert self.calc.division(8, 2) == 4

    def test_substraction_success(self):
        assert self.calc.subtraction(5, 2) == 3

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_pow_success(self):
        assert self.calc.pow(3, 2) == 9

    def test_sqrt_success(self):
        assert self.calc.sqrt(9, 0.5) == 3

    def teardown(self):
        print('Выполнение метода Teardown')
