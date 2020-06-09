from w3schools.import_ex.person import person
import w3schools.import_ex.person as p

age = person.get("age")

print(age)

p.greeting(person.get("name"))