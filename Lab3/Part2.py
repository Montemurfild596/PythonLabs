from pyDatalog import pyDatalog

"""
2 задание: посчитать среднее значение ряда из первого задания
"""

pyDatalog.create_terms('result, X')
result[X] = (X + 1) / 2
print(result[100]==X)