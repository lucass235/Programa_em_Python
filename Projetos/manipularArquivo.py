import shutil
from typing import Text


def escreverArquivo(texto):
    # criar o arquivo e fazer a primeira escrita
    diretorio = 'teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizarArquivo(nomeArquivo, texto):
    # escrever num arquivo existente

    arquivo = open(nomeArquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)


def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')  # abre o arquivo na variavel.
    alunoNota = arquivo.read()  # ler o arquivo.
    # print(alunoNota)
    # adiciona tudo que estiver em uma linha em um posicao da lista
    alunoNota = alunoNota.split('\n')
    # print(alunoNota)
    listaMedia = []
    for x in alunoNota:
        listaNotas = x.split(',')  # separa os elementos apartir da virgula.
        aluno = listaNotas[0]  # armazena o nome do aluno na variavel aluno
        listaNotas.pop(0)  # remover o nome do aluno na lista
        listaNotasI = int(listaNotas)
        media = sum(listaNotasI) / 4
        print(media)
        # listaMedia.append({aluno: media(listaMedia)})
    return listaMedia


def copiaArquivo(nomeArquivo, diretorio):
    import shutil
    shutil.copy(nomeArquivo, diretorio)


def moveArquivo(nomeArquivo, diretorio):
    shutil.move(nomeArquivo, diretorio)


if __name__ == '__main__':
    # copiaArquivo('notas.txt', 'home/lsa')
    listaMedia = mediaNotas('notas.txt')
    print(listaMedia)
    # mediaNotas('notas.txt')
    # escreverArquivo('Primeira linha. \n')
    # aluno = '\nCesar, 7, 9, 3, 8'
    # atualizarArquivo('notas.txt', aluno)
    # lerArquivo('teste.txt')
