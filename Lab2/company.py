import person
import employee
import client
import json
import copy

class Company:
    def __init__(self, name = "NOVALUE", employees = [], clients = []):
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

def SerializeCompany(company, path):    
    with open(path, 'w') as outfile:
        dict = copy.deepcopy(company.__dict__)
        dict["employees"] = [i.__dict__ for i in company.employees]
        dict["clients"] = [i.__dict__ for i in company.clients] 
        json.dump(dict, outfile, indent = 4, ensure_ascii = False)
    
def DeserializeCompany(path):
    def Deserialize(dict):        
        for i in Company().__dict__.keys():
            if not i in dict:   
                break
        else:
            return Company(dict["name"], [Deserialize(i) for i in dict["employees"]], [Deserialize(i) for i in dict["clients"]])
        for i in employee.Employee().__dict__.keys():
            if not i in dict:   
                break
        else:
            return employee.Employee(dict["surname"], dict["name"], dict["patronymic"], dict["age"], dict["salary"])
        for i in client.Client().__dict__.keys():
            if not i in dict:  
                break
        else:
            return client.Client(dict["surname"], dict["name"], dict["patronymic"], dict["age"], dict["order"])
    with open(path, 'r') as infile:
        data = json.load(infile)
        return Deserialize(data)