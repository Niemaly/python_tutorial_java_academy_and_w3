import json


class JsonFile:
    def __init__(self, name, path=""):
        self.name = f'{path}{name}.json'
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def save(self):
        return json.dumps(self.data)

    def load(self):
        pass


class BusinessCard:
    def __init__(self, name, surname, domain="mail.com"):
        self.name = name
        self.surname = surname
        self.email = f'{self.name}.{self.surname}@{domain}'
        self.no_want_this = "i dont want this in my json"

    def to_json(self):
        return {'name': self.name, "surname": self.surname, "email": self.email}


my_business_card = BusinessCard( "Jacek","Szumski")


def to_json(obj):
    return json.dumps(obj.to_json())


employees = [BusinessCard("Jacek", "Szumski").to_json(), BusinessCard("Wacław", "Pieniążek").to_json(),
             BusinessCard("Paweł", "Grabowski").to_json()]

json_file = JsonFile("employees")

json_file.add("employees", employees)
json_file.save()