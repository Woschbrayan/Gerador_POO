class Gerador:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.capacidade_maxima = capacidade_maxima
        self.capacidade_atual = 0

    def gerar(self, energia):
        if energia <= self.capacidade_maxima - self.capacidade_atual:
            self.capacidade_atual += energia
        else:
            print(f"Sobrecarga em {self.nome}!")

    def desligar(self):
        self.capacidade_atual = 0
