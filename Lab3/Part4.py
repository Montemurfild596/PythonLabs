from pyDatalog import pyDatalog
import random

"""

"""

pyDatalog.create_terms('median, summa_random_numbers, X')
summa_random_numbers[X] = random.randint(0, 100) + summa_random_numbers[X - 1]
summa_random_numbers[1] = random.randint(0, 100)
median[X] = summa_random_numbers[X] / X
print(median[100] == X)