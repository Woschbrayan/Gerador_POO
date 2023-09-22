# Gerador_POO
NOME: João Vitor Soares da Silva
RA: 2022101698

NOME: Yan Percegona Weiss
RA: 2022101667

NOME: Gustavo Almeida de Freitas
RA: 2022202287

NOME: Brayan Wosch
RA:2022100986

• Gerador – representa um gerador de energia. Deve ter os atributos nome,
capacidade_maxima e capacidade_atual e os métodos gerar(energia) e
desligar()
• Defina a classe Carga que representa a demanda de energia em MW. A classe deve ter os
atributos nome e energia e os métodos conectar() e desconectar()
• Crie a classe SistemaDeGeracao que representa o sistema de geração e consumo de
energia em MW. A classe deve ter como atributos uma lista de geradores (com objetos da
classe Gerador) e uma lista de demandas de energia (com objetos da classe Carga). Esta
classe deve ter também os métodos adicionar_gerador(gerador),
adicionar_carga(carga) e balancear(). O método balancear() deve ajustar
a energia gerada por cada gerador do sistema para atender à demanda exigida pelas cargas.
Em caso de sobrecarga a classe deve notificar o usuário do problema.
• (para obter a nota máxima) use o pytest e o coverage para gerar testes que cubram até
100% do código criado.

Usando a versão 1.0 do gerador da atividade anterior, use-o como base e crie a classe
GeradorQualificado (herdada da classe Gerador) para incluir os atributos:
• tipo_geracao (que pode ser hidrelétrica, eólica, solar ou termelétrica)
• custo_mw, indicando o custo de geração por MW
A classe deve incluir também o método:
• Exportar_dados : este método vai gerar um arquivo em formato CSV que poderá ser
aberto no Excel. Este arquivo conterá todos os resultados do balanceamento, incluindo os
geradores usados, cargas atendidas, capacidade usada e custo correspondente.
Crie a classe SistemaDeGeracaoVerde, herdada do SistemaDeGeracao, que use as
informações da nova classe GeradorQualificado para:
• priorizar acima de tudo o uso de energias limpas (só usar termelétricas se não houver
alternativa para atender à demanda)
• minimizar o custo respeitando na medida do possível a proteção ao meio ambiente.
• o sistema deve balancear automaticamente a geração de energia a cada inclusão de geradores
ou cargas (ao inserir, balanceia automaticamente).
• em caso de demanda maior do que a geração disponível o sistema deve desconectar uma ou
mais das cargas requisitadas até que a demanda esteja dentro do que é possível atender com
a matriz energética disponível. A classe deve informar ao usuário quais cargas foram
desconectadas quando isso for necessário.
• reportar os totais por tipo de geração e o respectivo custo médio por MW de cada tipo de
geração para a carga atual. Para isso crie um método que retorne um objeto do tipo dict()
contendo as informações solicitadas.
• (para obter a nota máxima) use o p•
Ao iniciar sem geradores, tentar conectar uma carga resulta em mantê-la na lista,
desconectada, com a classe reportando que a carga não foi atendida
• Ao conectar um gerador, se houverem cargas (conectadas ou não), deve-se balancear o
sistema para atender ao máximo de cargas possível, conforme os requisitos
• Os geradores devem ser usados por ordem de custo de geração de modo a minimizar o
custo, com prioridade pelo respeito ao meio-ambiente: usinas poluentes são a última escolha
independente de custo.
• Ao incluir um novo gerador com custo menor do que algum em uso (e que gere energia
limpa), balancear a carga de forma a aproveitá-lo.
