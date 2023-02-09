# Exception Handling

number_one = 5
number_two = 1

number_two = "1"

print(number_one + number_two)

# try except

number_tree = 5
number_four = 1

number_four = "1"

try:
    print(number_tree + number_four)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")