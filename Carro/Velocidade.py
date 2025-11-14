class Estatisticas:

    def __init__(self, velocidade, combustivel):
        self.velocidade = velocidade
        self.combustivel = combustivel

    def verificacaoVelocidade(self):
        if self.velocidade > 60:
            print("Vocês está acima da velocidade")
            return False
        else:
            print("Está baixo, matenha")
            return True

    def verificacaoCombustivel(self):
        if self.combustivel > 10:
            print("Você com uma boa quantidade de combustivel")
            return True
        else:
            print("Você tem uma baixa quantidade de combustivel")
            return False
