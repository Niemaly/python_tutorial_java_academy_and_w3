import json

class BusinessCard:
    def __init__(self, name, surname, domain="mail.com"):
        self.name = name
        self.surname = surname
        self.email = f'{self.name}.{self.surname}@{domain}'
        self.no_want_this = "i dont want this in my json"

    def to_jason(self):
        return {'name': self.name, "surname": self.surname, "email": self.email}

my_business_card = BusinessCard( "Jacek","Szumski")

def to_json(obj):
    return json.dumps(obj.to_jason())

print(to_json(my_business_card))