# Modules

import module

module.sumValue(5, 3, 4)


module.printValue("Hola Elunita!!")

from module import sumValue, printValue

sumValue(10, 9, 11)
printValue("Hola bebé")

# Importando módulo del sistema reservado de Python

import math

print(math.pi)
print(math.pow(2, 8))

# Cambiando el nombre de alguna función importada del sistema reservado de Python (No es obligatorio)

from math import pi  as PI_VALUE

print(PI_VALUE)