# Desafio de Operadores Lógicos
# Saber se a pessoa tem saldo positivo e acima de 20% do salario guardado

import os

saldo = 1000
salario = 4000
despesa = 2500

saldo_positivo = saldo > 0
despesa_controlada = salario - despesa >= 0.2 * salario
meta = saldo_positivo and despesa_controlada

os.system('cls')
print(meta)
