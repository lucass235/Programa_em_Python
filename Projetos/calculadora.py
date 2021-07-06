class Calculadora:  # classe calculadora
    def __init__(self):  # construtor da classe.
        pass

    def soma(self, valorA, valorB):  # funcao que retorna a soma dos atributos
        return valorA + valorB

    def subtracao(self, valorA, valorB):
        return valorA - valorB

    def multiplicacao(self, valorA, valorB):
        return valorA * valorB

    def divisao(self, valorA, valorB):
        return valorA / valorB


if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(10, 2))
    print(calculadora.divisao(100, 2))
    print(calculadora.multiplicacao(10, 5))
    print(calculadora.subtracao(5, 3))
