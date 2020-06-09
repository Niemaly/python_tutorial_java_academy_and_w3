from w3schools.classes.inheritance.person import Person


class Student(Person):
    def __init__(self, name, surname, graduationyear):
        super().__init__(name, surname)
        self.graduationyear = graduationyear

    def introduce(self):
        print("hello im ", self.name, self.surname, "im in class", self.graduationyear)


person = Person("Jacek", "Szumski")
student = Student("Jacek", "Placek", 2016)

person.printname()

student.printname()
student.introduce()