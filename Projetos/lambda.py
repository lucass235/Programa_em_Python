contadorLetras = lambda lista: [len(x) for x in lista]
listaAnimais = ['cachorro', 'gato', 'elefante']
print(contadorLetras(listaAnimais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b
print(soma(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma e: {}'.format(soma(10, 5)))
print('A multiplicacao e: {}'.format(multiplicacao(10, 2)))