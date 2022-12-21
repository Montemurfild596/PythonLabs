from company import *
from employee import *
from client import *
from person import *

company = Company("Магазин \"Шо та у Ашота\"", 
    [
        Employee("Омутных", "Олег", "Евгеньевич", 19, 355000),
        Employee("Зубенко", "Михаил", "Петрович", 34, 42000)
    ], 
    [
        Client("Собутыльников", "Иван", "Иванович", 40, "Ноутбук Asus 69.420"),
        Client("Светов", "Михаил", "-", 33, "Ребёнок")        
    ]);
SerializeCompany(company, "test.json")
print(company)
deserialized = DeserializeCompany("test.json")
print(deserialized)