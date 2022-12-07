import csv
import random
from collections import Counter
from itertools import takewhile

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

def generate_data_set(names, surnames, patronymics, cities):
	persons = list();
	persons.append(["ФИО", "Место жительства", "Зарплата"])
	for i in range(150):
		n_s_p = surnames[random.randint(0, len(surnames) - 1)] + " " + names[random.randint(0, len(names) - 1)] + " " + patronymics[random.randint(0, len(patronymics) - 1)]
		city = cities[random.randint(0, len(cities) - 1)]
		salary = random.randint(10000, 1000000)
		persons.append(n_s_p, city, salary)
	return persons

def write_CSV_from_list(source_dataset, file_name):
	with open(file_name, "w", newline="") as file:
		writer = csv.DictWriter(file, delimiter=',')
		writer.writerows(source_dataset)

def write_CSV_from_dict(source_dataset, file_name):
	with open(file_name, "w", newline="") as file:
		cols = list(source_dataset[0].keys())
		writer = csv.DictWriter(file, fieldnames=cols, delimiter=',')
		writer.writeheader()
		writer.writerows(source_dataset)

def read_csv(file_name):
	with open(file_name, "r", newline="") as file:
		reader = csv.DictReader(file)
		result = list()
		for i in reader:
			result.append(i)
	return result

def split nsp(source_dict):
	result = dict()
	strs = source_dict["ФИО"].split(' ')
	result["Фамилия"] = strs[0]
	result["Имя"] = strs[1]
	result["Отчество"] = strs[2]
	result["Место жительства"] = source_dict["Место жительства"]
	result["Зарплата"] = source_dict["Зарплата"]
	return result

def mode(x):
	most_common = Counter(x).most_common()
	if not most_common:
		return []
	else:
		max_count = most_common[0][1]
		return [x for x, count in takewhile(lambda x: x[1]==max_count, most_common)]


def get_most_city(source_dict_1):
	print("Самый часто встречающийся город: " + mode(source_dict_1["Зарплата"]))

