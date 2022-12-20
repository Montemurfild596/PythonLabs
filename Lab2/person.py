class Person:
	def __init__(self, surname = "NOVALUE", name = "NOVALUE", patronymic = "NOVALUE", age = 0):
		self.surname = surname
		self.name = name
		self.patronymic = patronymic
		self.age = age
	
	def __str__(self):
		return f"ФИО: {self.surname} {self.name} {self.patronymic}\tвозраст: {self.age}"

	