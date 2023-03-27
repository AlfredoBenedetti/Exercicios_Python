'''
CONDICIONAL SE - if

O condicional "se" possui três formas de aplicação, no entanto
para sua aplicação carece de algumas regras.

SINTAXE
Aqui detalho o caso mais complexo de utilização, preste atenção
na identação do código, conforme mencionamos anteriormente o python,
usa esta identação para identificar o que está dentro de cada instrução.

if(<condição_1>):
    <façaIsso>
elif(<condição_2>):
    <façaAquilo>
else:
    <facaUmaTerceiraCoisa>
'''
# CASO 1 - Analisa uma unica condição - caso simples(sem o "else").
# Aplica-se em verificações de resultados (tratamento de erros).

if (True):
    print("Faça isso")

# CASO 2 - Analisa as duas codições, se sim e o se não -
# caso comum (com "else").
# Aplica-se em casos que é necessário tratativas diferentes no fluxo.
a = 5
b = 3

if (a == b):
    print("A variável ""a"" é igual a ""b""")
else:
    print("A variável ""a"" é diferente de ""b""")

# CASO 3 - Analisa multiplas condições - caso de seleção (com "elif" e "else").
# Assim como um switch em C esse comando permite multiplos casos de aplicação.
if (a == b):
    print("A variável ""a"" é igual a ""b""")
elif (a > b):
    print("A variável ""a"" é maior que ""b""")
else:
    print("A variável ""a"" é menor que ""b""")
