from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, rodas, modelo, potencia):
        Veiculo.__init__(self, marca, rodas, modelo)
        self.potenciaDoMotor = potencia

    def imprimirInformacoes(self):
        print(self.__dict__)