''' 
     Conjuntos ou Sets, são similares as listas, porém possui diferenças marcantes.
        Elementos Únicos, Nao Indexado, Não Ordenado, Todos os elementos precisão ser
        imutáveis (Não aceita dicionários e listas), Possui diversos métodos baseados
        em lógica matemática de conjuntos (interseção, união, pertence, etc)
'''
import os

os.system('cls')
conjunto = {1, 2, 3, 4, 5}
print(type(conjunto))  # Irá exibir o tipo da função, no caso SET
print(conjunto)  # Irá exibir o conteúdo do conjunto
conjunto = set('Alfredo')  # conjunto irá receber um novo valor
print(conjunto)   # Irá exibir o valor do conjunto, porém a ordem não é garantida
print('A' in conjunto, 'B' not in conjunto)  # Operação IN funciona como esperado
conjunto = set('Alfredddo')  # conjunto irá receber um novo valor
print(conjunto)  # Irá exibir o conteúdo do conjunto, porém será exibido apenas uma letra D
print({1, 2, 3} == {3, 3, 2, 1})  # Numa comparação de igualdade, a ordem dos elementos não importa e as duplicações são ignoradas
a = {1, 2}
b = {2, 3}
a.union(b)  # Método UNION, retorna um novo set, porém não altera os set originais
print(a.intersection(b))  # Método INTERSECTION, retorna um novo set com a interseção dos elementos de a e b
a.update(b)  #  Método UPDATE, semelhante ao UNION, porém neste caso o set A sofre alteração
print(a)
print(b <= a)  # Indica que B contém todos os elementos de A, Verdadeiro pois a variável A sofreu altetação "a.update(b)"
print(a >= b)  # Indica que B contém todos os elementos de A, Verdadeiro pois a variável A sofreu altetação "a.update(b)"
print({1, 2, 4} - {2})  # Reatribui a diferença entre os conjuntos
print(a - b)
