import json
from abc import ABC, abstractmethod


class JsonFile:
    def __init__(self, name, path=""):
        self.name = f'{path}{name}.json'
        self.data = {}

    def add(self, data):
        self.data[data.__class__.__name__] = data.to_json()

    def save(self):
        return json.dumps(self.data)

    def load(self):
        pass


class Container(ABC):
    def __init__(self):
        self.content = []

    def add(self, value):
        self.content.append(value)

    @abstractmethod
    def to_json(self):
            pass


class BusinessCard:
    def __init__(self, name, surname, domain="mail.com"):
        self.name = name
        self.surname = surname
        self.email = f'{self.name}.{self.surname}@{domain}'
        self.no_want_this = "i dont want this in my json"

    def to_json(self):
        return {'name': self.name, "surname": self.surname, "email": self.email}


class Employees(Container):
    def to_json(self):
        return [business_card.to_json() for business_card in self.content]


my_business_card = BusinessCard( "Jacek","Szumski")


def to_json(obj):
    return json.dumps(obj.to_json())


employees = Employees()
list = [BusinessCard("Jacek", "Szumski"), BusinessCard("Wacław", "Pieniążek"),
        BusinessCard("Paweł", "Grabowski")]


for e in list:
    employees.add(e)

json_file = JsonFile("employees")

json_file.add(employees)

print(json_file.data)

# need to remember that self is an argument and can throw a TypeError!!