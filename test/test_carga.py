import sys
import pytest

sys.path.append("/home/joaosoares/mozard/PrejetoPOO")
from carga import Carga

def test_inicializacao_carga():
    carga = Carga("C1", 50)
    assert carga.nome == "C1"
    assert carga.energia == 50
    assert not carga.conectada

def test_conectar_carga():
    carga = Carga("C1", 50)
    carga.conectar()
    assert carga.conectada

def test_desconectar_carga():
    carga = Carga("C1", 50)
    carga.conectar()
    carga.desconectar()
    assert not carga.conectada

if __name__ == "__main__":
    pytest.main()
