import os

os.system('cls')

a = 'Alfredo'
b = 'Benedetti'

# Exemplo de textos com ASPAS

print("Marca D'Água")
print('Marca D\'Água')

# Exemplo de texto com Multiplas de Linhas
print("""Texto com
... Várias Linhas""")
print('''Texto com
... Várias Linhas''')
print('Texto com\nVárias linhas')
print('Texto com\tTAB')

nome = 'Alfredo Cezar Benedetti'
# Mostra na tela os 8 primeiros caracteres,
# lembrando que se inicia no 0 e o espaço também é contato.
print(nome[:7])   # Alfredo
print(nome[-5])   # d
print(nome[8:])   # Cezar Benedetti
print(nome[-9:])  # Benedetti
print(nome[14:], nome[0:13])  # Benedetti Alfredo Cezar
print(len(nome))  # Retorna a quantidade de caracteres na variável.

# Irá mostrar se a palavra deseja se encontra na String
print('Alfredo' in nome)         # True
print('alfredo' in nome)         # False, porque o pyrhon diferencia Maiuscula das Minisculas.
print(nome.lower())              # alfredo cezar benedetti
print('alfredo' in nome.lower())  # True, porque nome.lower alterou o escrito para minusculo.
print(nome.upper())              # ALFREDO CEZAR BENEDETTI
print(nome.split())              # ' Alfredo', 'Cezar', 'Benedetti'
print(b, a)                      # Benedetti Alfredo
