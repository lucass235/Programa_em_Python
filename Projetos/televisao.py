
class Televisao:
    def __init__(self):  # costrutor inicializa a tv desligada
        self.ligada = False
        self.canal = 9

    def power(self):  # procedimento para ligar ou desligar tv
        if self.ligada:  # condicao de estado da tv
            self.ligada = False
        else:
            self.ligada = True

    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1

    def diminuirCanal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':

    televisao = Televisao()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisao esta ligada: {}'.format(televisao.ligada))
    televisao.aumentaCanal()
    televisao.aumentaCanal()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisao esta ligada: {}'.format(televisao.ligada))
    televisao.aumentaCanal()
    televisao.diminuirCanal()
    print('Canal: {}'.format(televisao.canal))
