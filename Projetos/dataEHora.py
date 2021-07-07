# importacao da data do computador
from datetime import date, time, datetime, timedelta


def trabalhandoComDateTime():
    dataAtual = datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%d/%m/%y %H:%M:%S'))
    # traz a informacao completa de data e hora.
    print(dataAtual.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta',
             'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[dataAtual.weekday()])  # posicao do dia da semana
    dataCriada = datetime(2022, 6, 20, 15, 30, 20)
    print(dataCriada)
    print(dataCriada.strftime('%c'))
    dataString = '01/01/2019 15:20:22'
    dataConvertida = datetime.strptime(
        dataString, '%d/%m/%Y %H:%M:%S')  # converte string em data
    print(dataConvertida)

    novaData = dataConvertida - timedelta(days=365, minutes=18, seconds=3)
    print(novaData)


def trabalhandoComDate():
    dataAtual = date.today()
    print(dataAtual.strftime('%d/%m/%Y'))  # modificar saida da data
    dataAtualStr = dataAtual.strftime('%A %B %Y')  # modificar saida da data
    print(type(dataAtualStr))  # exibi o tipo da variavel
    print(type(dataAtual))


def trabalhandoComTime():
    horario = time(hour=14, minute=18, second=30)
    horarioStr = horario.strftime('%H:%M:%S')


if __name__ == '__main__':
    # trabalhandoComDate()
    # trabalhandoComTime()
    trabalhandoComDateTime()
