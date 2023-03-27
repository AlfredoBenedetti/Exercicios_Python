"""
Operadores ternários:
também conhecidos como expressões condicionais são operadores
que avaliam algo com base no fato de uma condição ser verdadeira ou falsa.
Ele simplesmente permite testar uma condição em uma única linha,
substituindo o if-else multilinha, tornando o código compacto.
"""

import os

# Exemplo 01

idade = input('Digite sua idade:')

if not idade.isnumeric():
    print('Digite sua idade')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Acesso Liberado' if maior else 'Acesso Negado'

# Exemplo 02

chovendo = False

os.system('cls')
print(msg)
print('Hoje estou com as roupas ' + ('secas', 'molhadas',)[chovendo])
print('Hoje estou com as roupas ' + ('molhadas' if chovendo else 'secas'))
