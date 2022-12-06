import csv
import random

def my_map(function, source_list):
	new_list = []
	for i in source_list:
		new_list.append(function(i))
	return new_list

def my_reduce(function, source_list):
	result = function(source_list[0], source_list[1])
	for i in source_list[2:]:
		result = function(result, i)
	return result