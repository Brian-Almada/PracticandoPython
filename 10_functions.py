# Functions

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(34, 123)
sum_two_values('5', '0')
sum_two_values(1.4, 5.6)


def new_funtion(num_1, num_2):
    return num_1 + num_2

my_result = new_funtion(432, 4274)
print(my_result)


def my_func(name, surname):
    print(f'{name} {surname}')

my_func("Brian", "Almada")
my_func(surname = "Messi", name = "GOAT")

def my_func(name, surname, age = 2):
    print(f'{name} {surname} {age}')

my_func("Izan", "Almada")

def print_upper_text(*texts): # Esto me indica que puedo tener la cantidad de parámetros que quiera sin necesidad de definirlos antes
    for text in texts:
        print(text.upper())

print_upper_text("Brian", "GOAT", "Argentina campeona", "Messi the best")