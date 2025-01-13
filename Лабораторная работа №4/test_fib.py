from main import EvenNumbersIterator, my_genn
import pytest


def test_with_3():
    gen = my_genn()
    next(gen)
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"


def test_with_0():
    gen = my_genn()
    next(gen)
    assert gen.send(0) == [], "Тест на ноль элементов, результат должен быть пустым списком"


def test_even_numbers_iterator_with_fib():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fib_iterator = EvenNumbersIterator(lst)
    assert list(fib_iterator) == [0, 1, 2, 3, 5, 8], "Должны быть извлечены все числа Фибоначчи из списка"


def test_even_numbers_iterator_with_no_fib_1():
    lst = [4, 6, 9, 10]
    fib_iterator = EvenNumbersIterator(lst)
    assert list(fib_iterator) == [], "Список не содержит чисел Фибоначчи, результат должен быть пустым списком"