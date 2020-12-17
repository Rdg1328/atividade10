from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro = False):
        Veiculo.__init__(self, marca, qtdRodas, modelo)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        print(' BICICLETA  Marca: {}  Qtd Rodas: {}, Modelo: {}  Qtd de marchas: {}  Bagageiro: {}'
              .format(self.marca, self.qtdRodas, self.modelo, self.numMarchas, self.bagageiro))
