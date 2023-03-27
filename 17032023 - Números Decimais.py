import os

from decimal import Decimal, getcontext
Valor = Decimal(1.1) + Decimal(2.2)

os.system('cls')
getcontext().prec = 3
print(Decimal(1.1) + Decimal(2.2))
