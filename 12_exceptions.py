# Exception Handling

# try except

number_tree = 5
number_four = 1

number_four = "1"

try:
    print(number_tree + number_four)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# capturando errores por su tipo

num_1 = "1"
num_2 = 2

try:
    print(num_1 + num_2)
    print("Se ejecuta el try si el programa va bien")
except TypeError:
    print("Se ejecuta si hay un TypeError")
except ValueError:
    print("Se ejecuta si hay un ValueError")


# Capturando el error

num_3 = 30
num_4 = 0

try:
    print(num_3 / num_4)
    print("Si está todo bien voy yo")
except ZeroDivisionError as error:
    print("Si alguien intenta dividir por 0 voy yo")
    print(error)