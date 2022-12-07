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

