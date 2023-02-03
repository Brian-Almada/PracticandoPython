#Sets
# Es una colección que no posee órden, y por tanto, tampoco números de índex

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Brian', 'Almada', 32}
print(type(my_other_set))

my_other_set.add('Programador')
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('Programador')
print(my_other_set) # Un set no admite repetidos

# IMPORTANTE: {} NO crea un conjunto vacío, sino un diccionario vacío. Usa set() si quieres crear un conjunto sin elementos

my_set = {'Pastelero'}
my_new_set = my_other_set.union(my_set)
print(my_new_set)