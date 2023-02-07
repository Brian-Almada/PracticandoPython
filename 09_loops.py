#Loops
#Es un mecanismo para poder iterar

# While

my_condition = 0

while my_condition < 10:
    print(my_condition) #Si hacemos el programa hasta esta línea se generarpá un bucle infinito
    my_condition += 2 # Con esta línea le ponemos un límite ya que vamos sumando hasta que en un momento sea mayor que diez y el condicional no se cumple y por tanto se detenga su ejecución


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se ejecuta el if")

    print(my_condition)