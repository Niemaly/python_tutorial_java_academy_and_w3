import json

class BusinessCard:
    def __init__(self, name, surname, domain="mail.com"):
        self.name = name
        self.surname = surname
        self.email = f'{self.name}.{self.surname}@{domain}'
        self.no_want_this = "i dont want this in my json"

my_business_card = BusinessCard( "Jacek","Szumski")

def to_json(obj):
    return json.dumps(obj.__dict__)

print(to_json(my_business_card))