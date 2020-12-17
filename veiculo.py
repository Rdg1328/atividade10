class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, vel):
        if vel != 0:
            self.velocidade += vel

    def frear(self, vel):
        if vel != 0:
            self.velocidade -= vel

        def imprimirInformacoes(self):
            print(self.__dict__)

