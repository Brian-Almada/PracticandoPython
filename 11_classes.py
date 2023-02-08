# Classes

#clase basía

class MyEmptyPerson:
    pass

print(MyEmptyPerson())

# creando clase con su constructor

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Brian", "Almada")

print(f"{my_person.name} {my_person.surname}")