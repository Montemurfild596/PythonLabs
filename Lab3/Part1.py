from pyDatalog import pyDatalog

"""
1 Задание: посчитать сумму ряда от 1 до 100
"""

pyDatalog.create_terms('result, X')
result[X] = (result[1] + X) * (X / 2)
result[1] = 1
print(result[9999999] == X)