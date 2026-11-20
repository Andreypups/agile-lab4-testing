import pytest

from math_module import factorial


# Перевіряємо факторіали невід'ємних цілих чисел.
def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_five():
    assert factorial(5) == 120


def test_factorial_seven():
    assert factorial(7) == 5040


# Перевіряємо помилки для неприпустимих значень.
def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_float():
    with pytest.raises(TypeError):
        factorial(2.5)
