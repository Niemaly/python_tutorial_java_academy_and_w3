from w3schools.classes.person import Person

class Car:
    def __init__(this, mark, model, age):
        this.mark = mark
        this.model = model
        this.age = age

    def register(this, person):
        this.person = person

car = Car("toyota", "corolla", 10)

person = Person("Jacek", "Szumski", 32)

car.register(person)

print(car.person.to_string())
