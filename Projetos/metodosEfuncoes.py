class Calculadora:
    def __init__(self, num1, num2):
        self.valorA = num1
        self.valorB = num2

    def soma(self):  # funcao que retorna a soma dos atributos
        return self.valorA + self.valorB

    def subtracao(self):
        return self.valorA - self.valorB

    def multiplicacao(self):
        return self.valorA * self.valorB

    def divisao(self):
        return self.valorA / self.valorB


calculadora = Calculadora(10, 2)
print(calculadora.valorB)
print(calculadora.soma())
print(calculadora.divisao())
print(calculadora.multiplicacao())
print(calculadora.subtracao())
