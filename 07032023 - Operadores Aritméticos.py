import os

# Variáveis
a1 = 10
a2 = 2

# Operação de Adição
# Realiza a soma de ambos operandos.
soma = a1 + a2

# Operação de Subtração
# Realiza a subtração de ambos operandos.
subtracao = a1 - a2

# Operação de Multiplicação
# Realiza a multiplicação de ambos operandos.
multiplicacao = a1*a2

# Operação de Divisão
# Realiza a Divisão de ambos operandos.
divisao = a1 / a2

# Operação de Módulo
# Em Python, % é o operador de módulo.
# Retorna o resto da divisão de ambos operandos.
modulo = a1 % a2

# Operador de exponenciação
# Retorna o resultado da elevação da potência pelo outro.
exponenciacao = a1 ** a2

# Divisão inteira
# Realiza a divisão entre operandos e a parte decimal de ambos operandos.
divisao_inteira = a1 // a2

os.system('cls')
print('Operação de Adição')
print('O resultado da Adição de ', a1, 'e', a2, 'é: ', str(soma))
print('')
print('Operação de Subtração')
print('O resultado da Subtração de ', a1, 'e', a2, 'é: ', str(subtracao))
print('')
print('Operação de Multiplicação')
print('O resultado da Multiplicação de ', a1, 'e', a2, 'é: ', str(multiplicacao))
print('')
print('Operação de Divisão')
print('O resultado da Divisão de ', a1, 'e', a2, 'é: ', str(divisao))
print('')
print('Operação de Módulo')
print('O resultado do Módulo de ', a1, 'e', a2, 'é: ', str(modulo))
print('')
print('Operação de Exponenciação')
print('O resultado da Exponenciação de ', a1, 'e', a2, 'é: ', str(exponenciacao))
print('')
print('Operação da Divisão Inteira')
print('O Resultado da Divisão Inteira de ', a1, 'e', a2, 'é: ', str(divisao_inteira))
