import person
class Client(person.Person):
    def __init__(self, surname = "NOVALUE", name = "NOVALUE", patronymic = "NOVALUE", age = 0, order= "NOVALUE"):
        super().__init__(surname, name, patronymic, age);
        self.order = order;

    def __str__(self):
        return super().__str__() + f"\tЗаказ: {self.order}";

    def __repr__(self):
        return "Client: " + self.__str__();