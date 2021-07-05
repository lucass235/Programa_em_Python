a = int(input('Digite o valor do primeiro bimestre: '))
if a > 10:
    a = int(input('Nota invalida, digite novamente: '))

b = int(input('Digite o valor do segundo bimestre: '))
if b > 10:
    b = int(input('Nota invalida, digite novamente: '))

c = int(input('Digite o valor do terceiro bimestre: '))
if c > 10:
    c = int(input('Nota invalida, digite novamente: '))

d = int(input('Digite o valor do quarto bimestre: '))
if d > 10:
    d = int(input('Nota invalida, digite novamente: '))

media = (a + b + c + d) / 4

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A media e : {}'.format(media))
# else:
#     print('Foi informado uma nota errada!')

# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# restoA = a % 2
# restoB = b % 2
# if restoA == 0 or restoB == 0:
#     print('Um numero par foi digitado')
# else:
#     print('Um numero impar foi digitado')

# a = int(input('Primeiro valor : '))
# b = int(input('Segundo valor : '))
# c = int(input('Terceiro valor : '))

# if a > b and a > c:
#     print('O maior numero e: {}'.format(a))
# elif b > a and b > c:
#     print('O maior numero e: {}'.format(b))
# else:
#     print('O maior numero e: {}'.format(c))
# print('Final do programa')
