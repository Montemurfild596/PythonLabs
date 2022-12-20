import person
import employee
import client
import json
import copy
#Компания
class Company:
    def __init__(self, nam = "NOVALUE", employees = [], clients = []):
        self.name = name    
        self.employees = employees
        self.clients = clients       

    def __str__(self):
        result = f"Компания: {self.name}\nРаботники:\n"
        for employee in self.employees:
            result += employee.__str__() + "\n"
        result += "Клиенты:\n"
        for client in self.clients:
            result += client.__str__() + "\n" 
        return result

    def __repr__(self):
        return self.__str__()