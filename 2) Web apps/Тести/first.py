import unittest

import pytest


# def add(x,y):
#    return x + y
#
# class TestAddition(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(3,5), 8)
#
#     def test_add_negative_number(self):
#         self.assertEqual(add(-1,-2), -3)
#
#     def test_add_zero(self):
#         self.assertEqual(add(0,0), 0)
#
#     def test_add_positive_negative_number(self):
#         self.assertEqual(add(-3,3), 0)

# @pytest.mark.parametrize('a, b, expected',
# [
#     (3,5,8),
#     (-1,-2,-3),
#     (0,0,0),
#     (-1,1,0),
# ])
# def test_add(a,b,expected):
#     assert add(a,b) == expected

# @pytest.fixture()
# def sample_list():
#     return [1,2,3,4,5]
#
# def test_sum(sample_list):
#     assert sum(sample_list) == 15
#
# def test_len(sample_list):
#     assert len(sample_list) == 5


# def calc(operation, a,b):
#     if operation == 'add':
#         return a + b
#     elif operation == 'sub':
#         return a - b
#     elif operation == 'mul':
#         return a * b
#     elif operation == 'div':
#         if b == 0:
#             raise ZeroDivisionError('Ділення на нуль')
#         return a / b
#     else:
#         raise ValueError(f'Невідома {operation} операція')
#
# print(calc('div', 4, 5))
#
# @pytest.mark.parametrize('operation, a, b, expected',
# [
#     ('mul', 2, 5, 10),
#     ('div', 20, 10, 2),
#     ('add', 8, 5, 13),
#     ('sub', 10, 15, -5),
# ])
# def test_call(operation,a,b,expected):
#     assert calc(operation,a,b) == expected

# def divide(a,b):
#     if b == 0:
#         raise ZeroDivisionError('Ділення на нуль')
#     return a / b
# def test_divide_success():
#     assert divide(10,2) == 5
#
# def test_divide_error():
#     with pytest.raises(ZeroDivisionError):
#         divide(10,0)


# import time
#
# def get_current_time():
#     return time.time()
#
# def test_get_current_time(monkeypatch):
#     fixed_time = 1609459200
#
#     def fake_time():
#         return fixed_time
#
#     monkeypatch.setattr(time,'time', fake_time)
#
#     assert get_current_time() == fixed_time

# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self,x):
#         self.value += x
#         return self.value
#
#     def substract(self,x):
#         self.value -= x
#         return self.value
# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         self.calc = Calculator()
#
#     def tearDown(self):
#         del self.calc
#
#     def test_add(self):
#         self.assertEqual(self.calc.add(5), 5)
#         self.assertEqual(self.calc.add(3), 8)
#     def test_subtract(self):
#         self.assertEqual(self.calc.substract(5), -5)


def to_upper(text):
    return text.upper()

def split_text(text, delimiter = ' '):
    if not isinstance(delimiter, str):
        raise TypeError('Роздільник повинен бути рядком')

    return text.split(delimiter)

def test_to_upper():
    assert to_upper('python') == 'PYTHON'


def test_split_text():
    text = 'hello world'
    assert split_text(text) == ['hello', 'world']

def test_split_text_error():
    with pytest.raises(TypeError):
        split_text('hello world', 2)