import os

# Variavéis
a = 10
b = 5

# Maior que:
# Este operador retorna Verdadeiro se o operando esquerdo for maior que o
# operando direito.
a > b

# Menor que:
# Este operador retorna Verdadeiro se o operando esquerdo for menor que o
# operando direito.
a < b

# Igual a:
# Este operador retorna Verdadeiro se ambos os operandos forem iguais,
# ou seja, se os operandos esquerdo e direito forem iguais um ao outro.
a == b

# Diferente de:
# Este operador retorna Verdadeiro se os dois operandos não forem iguais.
a != b

# Maior ou igual a:
# Este operador retorna Verdadeiro se o operando esquerdo for maior ou igual
# ao operando direito.
a >= b

# Menor ou igual a:
# Este operador retorna Verdadeiro se o operando esquerdo for menor ou igual
# ao operando direito.
a <= b

os.system('cls')
print(a, 'é MAIOR que:', b, a > b)
print(a, 'é MENOR que:', a < b)
print(a, 'é IGUAL a:', b, a == b)
print(a, 'é DIFERENTE de:', b, a != b)
print(a, 'é MAIOR ou IGUAL a:', b, a >= b)
print(a, 'é MENOR ou IGUAL a:', b, a <= b)
