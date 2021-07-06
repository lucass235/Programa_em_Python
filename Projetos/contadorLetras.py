def contadorLetras(listaPalavras):
    contador = []
    for x in listaPalavras:
        quantidade = len(x)  # informa o tamanho da string
        contador.append(quantidade)  # guarda na lista o tamanho de cada string
    return contador


def teste():
    return 'teste'


if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contadorLetras(lista))
