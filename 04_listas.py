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

# El método pop elimina el último elemento de la lista a menos que le indiquemos el índice que queremos quitar. Si imprimimos el pop veremos que nos retorna el índice que nos eliminó y podemos guardarlo en una variable si queremos

print(my_list) # lista original
print(my_list.pop()) # eliminación y retorno del último elemento de la lista
print(my_list) # lista modificada

my_pop_list = my_list.pop(2) # guardando en una variable el retorno del método pop al cual se le asignó un índice en especifico
print(my_pop_list)
print(my_list)

my_other_list.append(my_pop_list) # agregando el elemento que saqué de la otra lista
print(my_other_list)

my_new_list = my_list.copy() # copia los elementos de la lista y luego puedo guardarlos en una nueva

del my_list[2] # Elimina de la lista el elemento indicado y ya no retorna nada
print(my_list)

my_list.clear() # Limpia toda la lista dejandola sin elementos
print(my_list) # En este punto my_list quedó bacía
print(my_new_list) # En este punto tengo todo lo que tenía my_list antes de que se le deletearan y limpiaran los elementos

my_new_list.reverse() #Se orodena de atras para delante
print(my_new_list)

my_new_list.sort() #El método sort() nos permite ordenar una lista en orden ascendente ya que tiene un parámetro (reverse=False) que funciona por defecto.
print(my_new_list)

my_new_list.sort(reverse=True) #Pero si el reverse se valora en True la lista se ordena de forma descendente
print(my_new_list)

my_new_list.sort(key = None) # Otro parámetro en key que compara los elementos en su proceso de ordenamiento. Por defecto None lo hace de forma ascendente o alfabéticamente
print(my_new_list)

list_of_strings = ['hola', 'jajaja', 'no', 'sep', 'lluviasononon']
list_of_strings.sort(key = len) # En el caso de una lista con strings puedo mediante el método len ordenarlos por tamaño (cantidad de letras)
print(list_of_strings)
list_of_strings.sort(key = None) #Pero si le huvieramos dejado None lo haría alfabéticamente
print(list_of_strings)


