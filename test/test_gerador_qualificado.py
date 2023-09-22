import pytest
import os
import sys

sys.path.append("/home/joaosoares/mozard/PrejetoPOO")
from gerador_qualificado import GeradorQualificado

# Teste de criação de objeto GeradorQualificado
def test_gerador_qualificado_criacao():
    gq = GeradorQualificado("GQ1", 100, "Solar", 0.05)
    assert gq.nome == "GQ1"
    assert gq.capacidade_maxima == 100
    assert gq.tipo_geracao == "Solar"
    assert gq.custo_mw == 0.05
    assert gq.capacidade_atual == 0

# Teste do método gerar
def test_gerador_qualificado_gerar():
    gq = GeradorQualificado("GQ1", 100, "Solar", 0.05)
    gq.gerar(50)
    assert gq.capacidade_atual == 50

# Teste do método exportar_dados
def test_gerador_qualificado_exportar_dados():
    gq = GeradorQualificado("GQ1", 100, "Solar", 0.05)
    gq.gerar(50)
    gq.exportar_dados()

    # Verifique se o arquivo CSV foi criado
    assert os.path.isfile("GQ1_dados.csv")

# Função de limpeza após os testes
def teardown_module():
    # Remova os arquivos de teste gerados
    if os.path.isfile("GQ1_dados.csv"):
        os.remove("GQ1_dados.csv")

if __name__ == "__main__":
    pytest.main()
