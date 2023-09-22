from gerador import Gerador
from carga import Carga

class SistemaDeGeracao:
    def __init__(self):
        self.geradores = []
        self.cargas = []

    def adicionar_gerador(self, gerador):
        self.geradores.append(gerador)

    def adicionar_carga(self, carga):
        self.cargas.append(carga)

    def balancear(self):
        demanda_total = sum(carga.energia for carga in self.cargas)
        capacidade_total = sum(gerador.capacidade_maxima for gerador in self.geradores)

        if capacidade_total < demanda_total:
            print("Sobrecarga no sistema!")
            return

        self.geradores.sort(key=lambda gerador: gerador.capacidade_maxima, reverse=True)

        for carga in self.cargas:
            if carga.conectada:
                for gerador in self.geradores:
                    if gerador.capacidade_atual < gerador.capacidade_maxima and carga.energia > 0:
                        energia_fornecida = min(gerador.capacidade_maxima - gerador.capacidade_atual, carga.energia)
                        gerador.gerar(energia_fornecida)
                        carga.energia -= energia_fornecida

ps = SistemaDeGeracao()
g1 = Gerador("G1", 100)
g2 = Gerador("G2", 150)
c1 = Carga("C1", 60)
c2 = Carga("C2", 110)
c3 = Carga("C3", 80)
ps.adicionar_gerador(g1)
ps.adicionar_gerador(g2)
ps.adicionar_carga(c1)
ps.adicionar_carga(c2)
ps.adicionar_carga(c3)
c1.conectar()
c2.conectar()
c3.conectar()
ps.balancear()
print(f"{g1.nome}: {g1.capacidade_atual} MW")
print(f"{g2.nome}: {g2.capacidade_atual} MW")