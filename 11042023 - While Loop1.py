import os

# == while Loop == Excelente para Loops que depende de apenas uma condição

# Exemplo: Criar uma PROMOÇÂO para um produto no valor de R$ 100,00

os.system('cls')

Preco_Venda = 100
Preco_Custo = 25
Semana = 0

while Preco_Venda > Preco_Custo:
    Semana +=1
    print(f' Na semana {Semana} o produto vai ser vendido a R$ {Preco_Venda},00')
    Preco_Venda -=5
