class Person:
    def __init__(self, name,surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def to_string(self):
        return self.name + " "+ self.surname + " " +str(self.age)
