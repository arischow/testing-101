from unittest.mock import Mock


def add(*args):
    return sum(args)


def test_add():
    add_spy = Mock(wraps=add)

    result = add_spy(2, 3, 5)

    add_spy.assert_called_with(2, 3, 5)

    assert result == 10


class Calculator:
    def add(self, *args):
        return sum(args)


def test_calculator_add():
    calculator = Calculator()
    calculator.add = Mock(wraps=calculator.add)

    result = calculator.add(2, 3, 5)

    calculator.add.assert_called_with(2, 3, 5)

    assert result == 10


def test_calculator():
    calculator = Calculator()
    calculator_spy = Mock(wraps=calculator)

    result = calculator_spy.add(2, 3, 5)

    calculator_spy.add.assert_called_with(2, 3, 5)

    assert result == 10
