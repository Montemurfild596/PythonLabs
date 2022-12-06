import csv
import random

def my_map(function, source_list)
	new_list = []
	for i in source_list:
		new_list.append(function(i))
	return new_list