lista = [12, 10, 7, 5]
listaAnimal = ['cachorro', 'gato', 'elefante', 'logo', 'arara']
soma = 0

for x in listaAnimal:
    print(x)

for x in lista:
    print(x)
    soma += x
print(soma)

print(sum(lista))  # somar valores da lista
print(max(lista))  # maior valor da lista
print(min(lista))  # menor valor da lista
novaLista = listaAnimal * 3
print(novaLista)

if 'logo' in listaAnimal:
    print('existe um logo na lista')
else:
    print('nao existe um logo na lista. sera incluido!')
    listaAnimal.append('logo')  # add novo valor na lista
    print(listaAnimal)

listaAnimal.pop()  # retirar o ultimo valor da lista ou sua posicao.
print(listaAnimal)
listaAnimal.pop(0)
print(listaAnimal)

listaAnimal.remove('elefante')  # remove um elemento em especifico
print(listaAnimal)

lista.sort()  # ordena os elementos da lista.
listaAnimal.sort()
print(lista)
print(listaAnimal)

listaAnimal.reverse()  # ordena os elementos da lista em ordem inversa.
print(listaAnimal)

tupla = (1, 10, 12, 14)  # a tupla nao altera seus valores.
print(tupla)
print(tupla[1])
print(len(tupla))  # retorna a qtd de elementos na tupla ou lista.

tuplaAnimal = tuple(listaAnimal)  # converte o tipo lista em tupla.
listaNumerica = list(tupla)  # converte o tipo tupla em lista.
print(type(tuplaAnimal))  # exibi o tipo da variavel.
