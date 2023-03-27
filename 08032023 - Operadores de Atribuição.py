import os

# =: Operador de atribuição.
# Dada uma variável x, ao fazermos x = valor atribuímos o valor à variável x.
# Deste momento em diante, x é um sinônimo de valor.
# Por exemplo, se fizermos x = 5, ao imprimir x, o valor 5 será impresso.

x = 5

# +=: é equivalente a fazer a = a + valor.
# Por exemplo, se a valer 10 e fizermos a += 2, x passará a ter o valor 12.

a = 10
a += 2  # (a = a + 2) = 12

# -=, =, /=, //=, %=, *=:
# funcionam da mesma forma que o +=.
# Por exemplo, se x valer 5 e fizermos x *= 3 obteremos o valor 15. Na prática,
# o funcionamento desses operadores é o seguinte:
# x op= valor é equivalente a X = X OP VALOR,
# em que op é algum dos operadores listados anteriormente.

b = 10
b *= 5  # (b = b * 5) = 50

c = 10
c %= 3  # (c = c % 30) = 20

d = 6
d %= 4

e = 10
e -= 2

os.system('cls')
print(x)
print(a)
print(b)
print(c)
print(d)
print(e)
