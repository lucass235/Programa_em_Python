lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    # divisao = 10 / 0
    numero = lista[2]
    # x = a

except ZeroDivisionError:
    print('Nao e possivel realizar divisao por 0')
except IndexError:
    print('Erro ao acessar indice invalido')
except BaseException as ex:
    print('Erro desconhecido:  {}'.format(ex))
else:
    print('execucao bem sucedida')
finally:
    print('Sempre executa')
    arquivo.close()
