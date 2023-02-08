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

my_person = Person("Brian", "Almada") # Aquí estamos definiendo las propiedades por parámetro fuera del constructor

print(f"{my_person.name} {my_person.surname}")

# creando clase con propiedades definidas dentro del constructor

class OnePerson:
    def __init__(self):
        self.name = "Izan"
        self.surname = "Almada"

a_person = OnePerson()
print(f"{a_person.name} {a_person.surname}")