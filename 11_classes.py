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
        self.name = "Izan"  # Aquí las propiedades están definidas dentro del constructor y no pasados por parámetro
        self.surname = "Almada"

a_person = OnePerson()
print(f"{a_person.name} {a_person.surname}")

# creando clase con una propiedad en el constructor que almacena otras propiedades (como si fuera una variable)

class twoPerson:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}" # Aquí se usa una propiedad como variable para almacenar el resto de propiedades
    def walk(self): # Aquí podemos agregarle funciones a una clase (la cantidad que querramos)
        print(f"{self.full_name} Está caminando")

a_two_person = twoPerson("Eluney", "Almada")
print(a_two_person.full_name)

a_two_person.walk()