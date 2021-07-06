a = int(input('Digite o valor do primeiro bimestre: '))
while a > 10:
    a = int(input('Nota invalida, digite novamente: '))

b = int(input('Digite o valor do segundo bimestre: '))
while b > 10:
    b = int(input('Nota invalida, digite novamente: '))

c = int(input('Digite o valor do terceiro bimestre: '))
while c > 10:
    c = int(input('Nota invalida, digite novamente: '))

d = int(input('Digite o valor do quarto bimestre: '))
while d > 10:
    d = int(input('Nota invalida, digite novamente: '))
a = 0
while a <= 10:
    print(a)
    a += 1


for i in range(101):

    div = 0

    for x in range(1, i+1):
        resto = i % x
        if resto == 0:
            div += 1
    if div == 2:
        print('O numero {} e primo'.format(i))


a = int(input('digite um valor: '))

div = 0

for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1
if div == 2:
    print('O numero {} e primo'.format(a))
else:
    print('O numero {} nao e primo'.format(a))
