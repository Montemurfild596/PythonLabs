import person
class Client(person.Person):
    def __init__(self, surname : str = "NOVALUE", name : str = "NOVALUE", patronymic : str = "NOVALUE", age : int = 0, order : str = "NOVALUE"):
        super().__init__(surname, name, patronymic, age);
        self.order = order;