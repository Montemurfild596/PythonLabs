from pyDatalog import pyDatalog

"""
1 Задание: посчитать сумму ряда от 1 до 100
"""

pyDatalog.create_terms('result, X')
result[X] = X + result[X - 1]
result[1] = 1
print(result[100] == X)