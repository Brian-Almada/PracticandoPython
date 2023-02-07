#Conditionals
# Para que se ejecute el programa dentro del bloque del if deve ser verdadera la condición. Si es falsa no se ejecuta.
my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecición continúa")

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecición continúa")

# Otro ejemplo

my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecutara la condición si es verdadera") # Esta ejecución no se va a realizar porque 11 no cumple con la condición ya que decimos "Sí la variable my_condition es igual a 11 (el resultado de la multiplicación) entonces ejecutá el siguiente programa" Cómo 5 * 2 no es 11 sino 10, entonces la condición no se cumple. Por lo tanto el programa no se ejecuta a menos que cambiemos la condición y le digamos que if my_condition == 10

if my_condition > 10:
    print("Es mayor que 10")
else: #Con el else le decimos al condicional que si no se cumple de una forma se cumpla de esta manera
    print("Es menor o igual que 10")

my_condition = 5 * 3

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")