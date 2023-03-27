'''
Interpolação de String, Símbolos utilizados
     %s - String               %f - Real
     %d - Inteiro              %e - Real Exponencial
     %o - Octal                %% - Porcentagem
     %x - Hexacimal

Interpolações de Striing são extremamente úteis, podem ser simuladas utilizando concatenação
simples de strings, mas os resultados são muito inferiores que as que veremos abaixo.
     
'''

import os
from string import Template

nome, idade, salario = 'Alfredo C. Benedetti', 41, 1925.25
os.system('cls')

print('Nome: %s\nIdade: %d\nSalário: R$ %.2f' % (nome, idade, salario)) # método mais antigo
print()
print('Nome: {0}\nIdade: {1}\nSalário: R$ {2}'.format(nome, idade, salario)) # método até python 3.5
print()
print(f'Nome: {nome}\nIdade: {idade}\nSalário: R$ {salario}')  # Método a partir do Python 3.6

s = Template('Nome: $nome Idade: $idade Salário: $salario')
print(s.substitute(nome=nome, idade=idade, salario=salario))
