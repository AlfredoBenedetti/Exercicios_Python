from Funções import find_index
import os

os.system('cls')

list1 = ['a', 'b', 'c', 'd']

Letra = input('Entre com a Letra desejada: ')
Procura = find_index(list1, Letra)
print(Procura)
