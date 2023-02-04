#Dictionaries
#Es una estructura de datos que nos permite guardar parejas de claves y valores

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name":"Brian", "Surname":"Almada", "Age":32, 1:"Python" }

my_dict = {
    "Nombre":"Brian",
    "Apellido":"Almada",
    "Edad":32,
    "Lenguajes": {"Python", "JavaScript"},
    1:"Pastelero",
    2:"Programador"
}

print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])
my_dict["Nombre"] = "Alexis"
print(my_dict)

my_dict["Calle"] = "Mauricio Yadarola 2204"
print(my_dict)

print("Alexis" in my_dict) # Da False porque in busca keys no values
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict)
