import json
from abc import ABC, abstractmethod
from importlib import import_module as get_module


def get_class(core, source):
    try:
        return getattr(get_module(core.__module__), source.title())
    except Exception as e:
        print("exception : ", e)
        return getattr(get_module(core.__module__), core.__module__)


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

    def __str__(self):
        return f'{self.name}, {self.surname}, "email": {self.email}'


class Employees(Container):
    def to_json(self):
        pass

    def show(self):
        for employee in self.content:
            print(employee, "\n")


class Employee:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = get_class(self, position)()

    def get_business_card(self):
        return BusinessCard(self.name, self.surname)

    def __str__(self):
        return f"{self.position} {self.get_business_card()} \nsalary = {self.position.count_salary()}zł"


class Position(ABC):

    def __init__(self):
        self.salary_base = 2500

    @abstractmethod
    def position_bonus(self):
        pass

    @abstractmethod
    def premium(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def count_salary(self):
        return self.salary_base + self.position_bonus() + self.premium()


class President(Position):

    def premium(self):
        return self.salary_base * 3

    def position_bonus(self):
        return self.salary_base * 0.25


class Director(Position):

    def premium(self):
        return self.salary_base * 2.5

    def position_bonus(self):
        return self.salary_base * 0.2


class Manager(Position):

    def premium(self):
        return self.salary_base * 1.5

    def position_bonus(self):
        return 500


class Programmer(Position):

    def premium(self):
        return self.salary_base * 1

    def position_bonus(self):
        return self.salary_base * 0.1


class Worker(Position):

    def premium(self):
        return 500

    def position_bonus(self):
        return 0


class Cleaner(Position):

    def premium(self):
        return 0

    def position_bonus(self):
        return 0


employees = Employees()

list = [Employee("Jacek", "Szumski", "programmer"), Employee("Wacław", "Pieniążek", "manager"),
        Employee("Paweł", "Grabowski", "director")]


for e in list:
    employees.add(e)

employees.show()
