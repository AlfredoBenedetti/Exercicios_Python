import os

lista = ['Alice', 'Alfredo', 'Isabel', 'Cezar', 'Benedetti']

os.system('cls')

print(lista)
a = input('Digite um nome\n')
print(lista.index(a))
print(lista[-1])
print('Alice' in lista)
print('Pablo' not in lista)
print(lista[::3])
del lista[2]
print(lista)
del lista[1:]
print(lista)
