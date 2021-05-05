import person
class Employee(person.Person):
	def __init__(self, surname = "NOVALUE", name = "NOVALUE", patronymic = "NOVALUE", age = 0, salary = 0):
		super().__init__(surname, name, patronymic, age)
		self.salary = salary

	def  __str__(self):
		return super().__str__() + f"\tДоход: {self.salary}"

	def __repr__(self):
		return "Employee: " + self.__str__()