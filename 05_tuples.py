#Tuples
#son colecciones de datos idénticos o distintos clasificados con un índice y que no pueden ser modificados, son inmutables.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (32, 1.89, 'Brian', 'Almada')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count('Brian'))

#my_tuple.append('Brian') Las tuplas no pueden ser modificadas
#my_tuple.insert(3, 'Brian') Las tuplas no pueden ser modificadas

my_other_tuple = ('Pastelero', 'Programador')

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


