# comando para pegar o valor do usuario, convertendo ele em um inteiro.
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B : '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
soma = str(soma)  # converte a variavel soma em uma string

print('soma: ' + soma)
print('soma com format: {}'.format(soma))  # outra maneira de formatar a saida.
print('subtracao: ' + str(subtracao))
print('multiplicacao: ' + str(multiplicacao))
divisao = int(divisao)  # converte a variavel divisao em um inteiro.
print('divisao: ' + str(divisao))
print('resto: ' + str(resto))
print('===================================================================')
print('Soma: {so} \nSubtração: {su} \nMultiplicação: {mu} \nDivisão {di} \nResto: {re}'
      .format(so=soma, su=subtracao, mu=multiplicacao,
              di=divisao, re=resto))  # outra forma de print de variaveis

x = '1'
x = int(x)  # converte a variavvel x em um inteiro
soma2 = x + 1
print(soma2)
