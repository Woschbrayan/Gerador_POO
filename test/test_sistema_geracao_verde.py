import sys
import pytest

sys.path.append("/home/joaosoares/mozard/PrejetoPOO")
from sistema_geracao_verde import SistemaDeGeracaoVerde
from gerador_qualificado import GeradorQualificado
from carga import Carga

def test_sistema_de_geracao_verde_criacao():
    sistema = SistemaDeGeracaoVerde()
    assert len(sistema.geradores) == 0
    assert len(sistema.cargas) == 0

def test_sistema_de_geracao_verde_adicionar_gerador():
    sistema = SistemaDeGeracaoVerde()
    gerador = GeradorQualificado("G1", 100, "Solar", 0.05)
    sistema.adicionar_gerador(gerador)
    assert len(sistema.geradores) == 1
    assert sistema.geradores[0] == gerador

def test_sistema_de_geracao_verde_adicionar_carga():
    sistema = SistemaDeGeracaoVerde()
    carga = Carga("C1", 50)
    sistema.adicionar_carga(carga)
    assert len(sistema.cargas) == 1
    assert sistema.cargas[0] == carga

def test_sistema_de_geracao_verde_balancear():
    sistema = SistemaDeGeracaoVerde()
    gerador = GeradorQualificado("G1", 100, "Solar", 0.05)
    carga = Carga("C1", 50)
    sistema.adicionar_gerador(gerador)
    sistema.adicionar_carga(carga)
    sistema.balancear()
    assert gerador.capacidade_atual == 0

def test_sistema_de_geracao_verde_relatorio_geracao_por_tipo():
    sistema = SistemaDeGeracaoVerde()
    gerador_solar = GeradorQualificado("G1", 100, "Solar", 0.05)
    gerador_eolico = GeradorQualificado("G2", 150, "Eólica", 0.03)
    carga = Carga("C1", 50)
    sistema.adicionar_gerador(gerador_solar)
    sistema.adicionar_gerador(gerador_eolico)
    sistema.adicionar_carga(carga)
    sistema.balancear()
    relatorio = sistema.relatorio_geracao_por_tipo()

    assert relatorio["Eólica"]["capacidade"] == 0
    assert relatorio["Eólica"]["custo_total"] == 0
    assert relatorio["Solar"]["custo_medio"] == 0
    assert relatorio["Eólica"]["capacidade"] == 0
    assert relatorio["Eólica"]["custo_total"] == 0
    assert relatorio["Eólica"]["custo_medio"] == 0

if __name__ == "__main__":
    pytest.main()
