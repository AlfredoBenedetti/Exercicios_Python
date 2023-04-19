import os

# Exemplo: Enviar uma mensagem com os detalhes da compra online
# com no máximo 3 tentativas para compra confirmada

os.system('cls')

compra = True
dado = 'COMPRA REALIZADA COM SUCESSO'

for enviar in range(3):
    if compra:
        print(dado)
        print('\nDETALHES ENVIADOS PARA O EMAIL CADASTRADO')
    break
else:
    print('FALHA NA COMPRA')
