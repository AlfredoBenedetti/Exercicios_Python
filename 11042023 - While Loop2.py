import os

# == while Loop == Excelente para Loops que depende de apenas uma condição

# Exemplo: Publicar um Produto com uma comissão de 10% para Produtos acima de R$ 20,00

os.system('cls')

Valor_Produto = int(input('Fazer inserir o Valor do Produto a Venda R$'))
Comissao = Valor_Produto * 0.1

os.system('cls')

while Valor_Produto > 20:
    Valor_Produto = Valor_Produto + Comissao
    print(f'O Valor do seu Produto será vendido em Nossa Plataforma por R${Valor_Produto}')
    print(f'R$ {Comissao} de Comissão da Plataforma')
    break
