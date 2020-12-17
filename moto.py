from Veiculo import Veiculo
from Automovel import Automovel

class Moto(Automovel, Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potencia, partidaEletrica = False):
        Veiculo.__init__(self, marca, qtdRodas, modelo, potencia)
        Automovel.__init__(self, potencia)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        print('MOTO  Marca: {}  Qtd Rodas: {}  Modelo: {}, Potencia do motor: {}  Partida Eletrica: {}'
              .format(self.marca, self.qtdRodas, self.modelo, self.potMotor, self.partidaEletrica))