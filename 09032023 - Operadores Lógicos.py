
# Esses Operadores nos possibilitam construir um tipo de teste muito útil
# e muito utilizado em qualquer programa Python: os testes lógicos.

# Python nos disponibiliza três tipos de Operadores Lógicos:
# o and, o or e o not.

# Vamos ver mais sobre eles agora!

#    Operador	                    Definição
#      and	       Retorna True se ambas as afirmações forem verdadeiras
#       or	       Retorna True se uma das afirmações for verdadeira
#      not	       Retorna Falso se o resultado for verdadeiro

import os

a = 7
b = 4

os.system('cls')

# Tabela Verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True and True and True and False and True and True)
print('')
# Tabela Verdade do Or
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(True or True or True or False or True)
print('')
# Tabela Verdade do XOR - OR Exclusivo - != Diferente
print(True != True)
print(True != False)
print(False != True)
print(False != False)
print('')
# Operação de Negação - Unário
print(not True)
print(not False)
print('')
# Exemplo and
if a > 3 and b < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
if a > 4 or b <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
if not (a < 10 and b < 8):
    print('Inverte o resultado da condição entre os parânteses')
