#Operadores

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(3 // 4)
print(2 ** 3)

print("Hola" + " Python")

#Operadores comparativos con int
print(4 < 3)
print(4 > 3)
print(5 <= 3)
print(5 >= 3)
print(6 == 7)
print(6 != 7)

#Operadores comparativos con str
print("Hola" < " Python")
print("Hola" > " Python")
print("Hola" <= " Python")
print("Hola" >= " Python")
print("Hola" == " Python")
print("Hola" != " Python")

#Operadores lógicos

# and: Devuelve True si ambos operandos son True

print(3 > 4 and "Hola" > "Python") #---> False and False = False
print(3 < 4 and "Hola" < "Python") #---> True and True = True
print(3 < 4 and "Hola" > "Python") #---> True and False = False

# or: Devuelve True si alguno de los operandos es True

print(3 > 4 or "Hola" < "Python") #---> False or True = True
print(3 > 4 and "Hola" > "Python") #---> False and False = False
print(3 < 4 and "Hola" < "Python") #---> True and True = True

# not: Devuelve True si alguno de los operandos es False

print(not(3 > 4)) #---> False = True
print(not(3 < 4)) #---> True = False