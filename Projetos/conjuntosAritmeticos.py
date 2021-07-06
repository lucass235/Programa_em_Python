conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
print('Conjunto1: {}'.format(conjunto))
print('Conjunto2: {}'.format(conjunto2))
conjuntoUniao = conjunto.union(conjunto2)  # faz a uniao dos conjuntos
print('Uniao: {}'.format(conjuntoUniao))
conjuntoInterseccao = conjunto.intersection(
    conjunto2)  # faz a interseccao dos conjuntos
print('Interseccao: {}'.format(conjuntoInterseccao))
conjuntoDiferenca = conjunto.difference(
    conjunto2)  # faz a diferenca dos conjuntos
print('Diferenca: {}'.format(conjuntoDiferenca))

conjuntoDiffSimetrica = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}'.format(conjuntoDiffSimetrica))

conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}
# retorna um valor booleano referente se aquele e um subconjunto do outro
conjuntoSubset = conjuntoA.issubset(conjuntoB)
print(conjuntoSubset)

conjuntoSuperset = conjuntoB.issuperset(conjuntoA)
print(conjuntoSuperset)

lista = ['cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjuntoAnimaisL = set(lista)  # converte o conjuto em lista.
print(conjuntoAnimaisL)

# conjunto = {1, 2, 3, 4}  # conjuntos nao repete valores
# conjunto.add(5)  # add valor no conjunto
# conjunto.discard(2)  # remover valor do conjunto
# print(type(conjunto))
# print(conjunto)
