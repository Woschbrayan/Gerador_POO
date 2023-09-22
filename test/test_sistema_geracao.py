import sys
import pytest


sys.path.append("/home/joaosoares/mozard/PrejetoPOO")
from gerador import Gerador
from carga import Carga
from sistema_geracao import SistemaDeGeracao

def test_balanceamento_de_energia():
    ps = SistemaDeGeracao()
    g1 = Gerador("G1", 90)
    g2 = Gerador("G2", 150)
    c1 = Carga("C1", 50)
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
    assert g1.capacidade_atual == 90
    assert g2.capacidade_atual == 150

def test_sobrecarga_no_sistema():
    ps = SistemaDeGeracao()
    g1 = Gerador("G1", 90)
    c1 = Carga("C1", 200)
    ps.adicionar_gerador(g1)
    ps.adicionar_carga(c1)
    c1.conectar()
    ps.balancear()
    assert g1.capacidade_atual == 0

if __name__ == "__main__":
    pytest.main()
