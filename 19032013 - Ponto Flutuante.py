#Mais Informações - https://docs.python.org/3/library/decimal.html

import os

from decimal import Decimal, getcontext
getcontext().prec = 6

os.system('cls')

valor1 = Decimal(1) / Decimal(7)
print(valor1)
# Decimal('0.142857')

getcontext().prec = 28
valor2 = Decimal(1) / Decimal(7)
# Decimal('0.1428571428571428571428571429')
print(valor2)
