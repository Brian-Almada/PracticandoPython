#Lists
# nota: La lista ya no es una base sino una estructura
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 55, 57, 88, 54, 646, 44, 88, 45]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.89, 'Brian', 'Almada']

print(type(my_list))
print(type(my_other_list))

#print(my_other_list[4]) IndexError: list index out of range (indice fuera de rango)
print(my_other_list[3])
print(my_other_list[2])
print(my_other_list[1])
print(my_other_list[0])
#print(my_other_list[-5]) IndexError: list index out of range (indice fuera de rango)
print(my_other_list[-4])
print(my_other_list[-3])
print(my_other_list[-2])
print(my_other_list[-1])

print(my_list.count(88)) # El método count retorna el número de ocurrencias que tiene un valor
age, height, name, surname = my_other_list #Desempaquetado
print(name)
print(age)
print(my_list + my_other_list) # Concatenado de listas
my_other_list.append("Programador") # Agrega un elemento a la lista en el último lugar
print(my_other_list)
my_other_list.insert(4, "Pastelero") # Agrega un elemento a la lista en la posición elegida
print(my_other_list)
my_other_list.remove("Pastelero")
print(my_other_list)