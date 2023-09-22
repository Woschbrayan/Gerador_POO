import csv
from gerador import Gerador

class GeradorQualificado(Gerador):
    def __init__(self, nome, capacidade_maxima, tipo_geracao, custo_mw):
        super().__init__(nome, capacidade_maxima)
        self.tipo_geracao = tipo_geracao
        self.custo_mw = custo_mw
        self.registros = []

    def gerar(self, energia):
        super().gerar(energia)
        carga_atendida = min(energia, self.capacidade_maxima - self.capacidade_atual)
        custo = carga_atendida * self.custo_mw
        self.registros.append([self.nome, carga_atendida, self.capacidade_atual, custo])

    def exportar_dados(self):
        with open(f"{self.nome}_dados.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Gerador", "Carga Atendida (MW)", "Capacidade Usada (MW)", "Custo (R$)"])
            writer.writerows(self.registros)
