from pyDatalog import pyDatalog
import random

"""
3 Задание: посчитать произведение 100 чисел, созданных с помощью датчика случайных чисел
"""

pyDatalog.create_terms('multiplication_random_numbers, X')
multiplication_random_numbers[X] = random.randint(0, 100) * multiplication_random_numbers[X - 1]
multiplication_random_numbers[1] = random.randint(0, 100)
print(multiplication_random_numbers[100] == X)