import pytest
from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    # add positive
    def test_adding_success(self):
        assert self.calc.adding(self, 10, 5) == 15

    # subtraction positive
    def test_substraction_success(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    # division positive
    def test_div_success(self):
        assert self.calc.division(self, 10, 5) == 2

    # multiply positive
    def test_mult_success(self):
        assert self.calc.multiply(self, 10, 5) == 50

    def teardown_method(self):
        print("Выполнение метода Teardown: задание 24.2.3 - позитивные тесты для каждого метода калькулятора")
