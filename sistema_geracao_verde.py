from sistema_geracao import SistemaDeGeracao
from gerador_qualificado import GeradorQualificado
from carga import Carga

class SistemaDeGeracaoVerde(SistemaDeGeracao):
    def __init__(self):
        super().__init__()

    def balancear(self):
        self.geradores.sort(key=lambda gerador: (gerador.custo_mw, gerador.tipo_geracao))

        for carga in self.cargas:
            carga.conectada = False

        demanda_total = sum(carga.energia for carga in self.cargas if not carga.conectada)

        for gerador in self.geradores:
            gerador.capacidade_atual = 0

        if demanda_total == 0:
            return

        for carga in self.cargas:
            if carga.energia <= 0:
                continue
            for gerador in self.geradores:
                if gerador.capacidade_atual < gerador.capacidade_maxima and carga.energia > 0:
                    energia_fornecida = min(gerador.capacidade_maxima - gerador.capacidade_atual, carga.energia)
                    gerador.gerar(energia_fornecida)
                    carga.energia -= energia_fornecida
                    carga.conectada = True

    def adicionar_gerador(self, gerador):
        super().adicionar_gerador(gerador)
        self.balancear()

    def adicionar_carga(self, carga):
        super().adicionar_carga(carga)
        self.balancear()

    def relatorio_geracao_por_tipo(self):
        relatorio = {}
        for gerador in self.geradores:
            if gerador.tipo_geracao in relatorio:
                relatorio[gerador.tipo_geracao]["capacidade"] += gerador.capacidade_atual
                relatorio[gerador.tipo_geracao]["custo_total"] += gerador.capacidade_atual * gerador.custo_mw
            else:
                relatorio[gerador.tipo_geracao] = {
                    "capacidade": gerador.capacidade_atual,
                    "custo_total": gerador.capacidade_atual * gerador.custo_mw,
                }

        for tipo, dados in relatorio.items():
            if dados["capacidade"] > 0:
                dados["custo_medio"] = dados["custo_total"] / dados["capacidade"]
            else:
                dados["custo_medio"] = 0

        return relatorio

g1 = GeradorQualificado("G1", 150, "Eólica", 0.05)
g1.gerar(50)
g1.gerar(30)
g1.exportar_dados()

print(f"Arquivo CSV criado com sucesso!")
