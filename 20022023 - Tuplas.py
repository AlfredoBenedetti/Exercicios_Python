# As Tuplas são similares a lista porém são imutáveis.

# Exemplos

tupla = tuple
print(tupla)  # Tupla vazia, a partir da chamada da classe Tuple
tupla = ('Alfredo',)
# Diferente das listas, as tuplas possuem poucos métodos, e estes fucionam de forma similar às listas

cores = ('amarelo', 'azul', 'vermelho', 'preto', 'branco', 'preto')
print(tupla)
print(cores[0])   # Mostra o item do local 0
print(cores[-1])  # Mostra o item da última posição
print(cores[1:])  # Mostra os itens a partir da posição 1
print(cores.index('amarelo'))  # Mostra o local onde está localizado on item desejado
print(cores.count('preto'))  # Mostra a quantidade de itens existente da tupla
print(len(cores)) # Mostra a quantidade de itens existente na tupla
