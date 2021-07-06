from televisao import Televisao
from calculadora import Calculadora
from contadorLetras import contadorLetras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora()
    print(calculadora.soma(10, 5))

    lista = ['cachorro', 'gato', 'elefante']
    totalLetras = contadorLetras(lista)
    print(totalLetras)
