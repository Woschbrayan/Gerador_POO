import sys
import pytest

sys.path.append("/home/joaosoares/mozard/PrejetoPOO")
from gerador import Gerador

def test_inicializacao_gerador():
    gerador = Gerador("G1", 100)
    assert gerador.nome == "G1"
    assert gerador.capacidade_maxima == 100
    assert gerador.capacidade_atual == 0

def test_gerar_energia():
    gerador = Gerador("G1", 100)
    gerador.gerar(50)
    assert gerador.capacidade_atual == 50

def test_sobrecarga_gerador():
    gerador = Gerador("G1", 100)
    gerador.gerar(150)
    assert gerador.capacidade_atual == 0

def test_desligar_gerador():
    gerador = Gerador("G1", 100)
    gerador.gerar(50)
    gerador.desligar()
    assert gerador.capacidade_atual == 0

if __name__ == "__main__":
    pytest.main()
