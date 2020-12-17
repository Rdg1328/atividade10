from Veiculo import Veiculo
from Automovel import Automovel

class Carro(Automovel, Veiculo):
    def __init__(self, marca, rodas, modelo, potencia, qtdPortas):
        Automovel.__init__(self, potencia)
        Veiculo.__init__(self, marca, rodas, modelo, potencia)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        print(' CARRO   Marca: {}   Numero de rodas: {}, Modelo: {}  Potencia do motor: {}   Numero de portas: {}'
              .format(self.marca, self.qtdRodas, self.modelo,
                      self.potMotor, self.qtdPortas))
