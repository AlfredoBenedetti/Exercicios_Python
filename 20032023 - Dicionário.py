import os
cadastro = {'nome': 'Alfredo Cezar Benedetti', 'idade': 41, 'profissão': ['Programador', 'Analista de Sistema']}
os.system('cls')
print(type(cadastro))  # Mostra o tipo da função, (dict) no caso dicionário
print(len(cadastro))   # Mostra a quantidade de itens armazenado no dicionário
print(cadastro['nome'])  # Exibe o valor relacionado a chave nome (Alfredo Cezar Benedetti)
cadastro['profissão'].append('Analista SAP')
print(cadastro.keys())    # Exibe apenas as chaves armazenadas no dicionário
print(cadastro.values())  # Exibe apenas os valores armazenados no dicionário
print(cadastro.items())   # Exibe todos os itens armazenados no dicionário
print(cadastro.get('idade'))  # Exibe o valor relacionado a chave idade (41)
cadastro['profissão'].append('JavaScript')  # Insere um novo item no dicionário, no caso o valor foi inserino na chave Profissão
print(cadastro)
print(cadastro['profissão'])  # Irá exibir apenas as informações da chave desejada
cadastro.update({'idade': 42, 'sexo': 'Masculino'})  # Irá atualizar o dicionário com as novas informações
print(cadastro)
del cadastro['sexo']  # Irá deletar as informações relacionada a chave
print(cadastro)
cadastro.clear() # Irá apagar todas as informações do dicionário
print(cadastro)
