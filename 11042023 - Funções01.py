import os

# == Funções == 

# DRY - Don´t Repeat Yourself
# Parametro --> Argumento

os.system('cls')

def soma():
    n1 = 10
    n2 = 5
    resultado = n1 + n2
    print(resultado)

def multiplica():
    n1 = 10
    n2 = 5
    resultado = n1 * n2
    print(resultado)

soma()
multiplica()
