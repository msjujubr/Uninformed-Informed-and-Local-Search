# Busca Não Informada, Busca Informada e Busca Local

![Python](https://img.shields.io/badge/LANG-Python-green.svg)
![VSCode](https://img.shields.io/badge/IDE-VSCode-informational)
![ISO](https://img.shields.io/badge/ISO-Linux-blueviolet)

- **Aluno(a):** `Júlia de Moura Souza`
- **Repositório Git:** [`link do repositório`](https://github.com/msjujubr/Uninformed-Informed-and-Local-Search)
- **Tag:** `entrega-parte1` ou `entrega-final`

  - **Parte 1 - Busca não informada e informada:** entrega em **08/10/2026**.
    
  - **Parte 2 - Busca local e entrega final:** entrega em **15/10/2026**.

<div align="center"> <table> <tr> <td>
 
# 📖 Sumário

* [Sobre o Projeto](#sobre-o-projeto)

* [Especificação do Problema](#especificação-do-problema)

  * [Parte 1 — Busca em Ambiente Ponderado](#parte-1--busca-em-ambiente-ponderado)
  * [Parte 2 — Problema das 8 Rainhas](#parte-2--problema-das-8-rainhas)

* [Estrutura do Projeto](#estrutura-do-projeto)

  * [Organização dos Arquivos](#organização-dos-arquivos)
  * [Mapas e Dados de Entrada](#mapas-e-dados-de-entrada)
  * [Testes](#testes)
  * [Resultados](#resultados)

* [Algoritmos Implementados](#algoritmos-implementados)

  * [Busca em Largura — BFS](#busca-em-largura--bfs)
  * [Busca em Profundidade — DFS](#busca-em-profundidade--dfs)
  * [Busca de Custo Uniforme — UCS](#busca-de-custo-uniforme--ucs)
  * [Busca Gulosa](#busca-gulosa)
  * [A*](#a)
  * [Hill Climbing](#hill-climbing)
  * [Random-Restart Hill Climbing](#random-restart-hill-climbing)

* [Heurísticas](#heurísticas)

  * [Heurística de Manhattan](#heurística-de-manhattan)
  * [Heurística Euclidiana](#heurística-euclidiana)

* [Regras de Busca](#regras-de-busca)

  * [Ordem dos Sucessores](#ordem-dos-sucessores)
  * [Critérios de Desempate](#critérios-de-desempate)
  * [Tratamento de Estados Repetidos](#tratamento-de-estados-repetidos)

* [Compilação, Instalação e Execução](#compilação-instalação-e-execução)

  * [Requisitos](#requisitos)
  * [Instalação](#instalação)
  * [Execução da Parte 1](#execução-da-parte-1)
  * [Execução da Parte 2](#execução-da-parte-2)
  * [Reprodução dos Resultados](#reprodução-dos-resultados)

* [Entradas e Saídas](#entradas-e-saídas)

  * [Formato do Mapa](#formato-do-mapa)
  * [Saída dos Algoritmos de Busca](#saída-dos-algoritmos-de-busca)
  * [Saída dos Experimentos](#saída-dos-experimentos)

* [Testes](#testes)

  * [Início Adjacente ao Objetivo](#início-adjacente-ao-objetivo)
  * [Mapa Sem Solução](#mapa-sem-solução)
  * [Mapa com Ciclos](#mapa-com-ciclos)
  * [Rotas com Mesmo Número de Ações](#rotas-com-mesmo-número-de-ações)
  * [Rota Curta e Cara vs. Rota Longa e Barata](#rota-curta-e-cara-vs-rota-longa-e-barata)

* [Métricas e Resultados](#métricas-e-resultados)

  * [Métricas da Parte 1](#métricas-da-parte-1)
  * [Experimentos das 8 Rainhas](#experimentos-das-8-rainhas)
  * [Sementes Utilizadas](#sementes-utilizadas)

* [Reprodutibilidade](#reprodutibilidade)

  * [Versões das Entregas](#versões-das-entregas)
  * [Tags do Repositório](#tags-do-repositório)

* [Uso de Inteligência Artificial](#uso-de-inteligência-artificial)

* [Referências](#referências)



# Sobre o Projeto

Este projeto foi desenvolvido para a disciplina **Inteligência Artificial** do CEFET-MG (Campus Divinópolis), sob a orientação do [Prof. Tiago Alves de Oliveira](https://github.com/tiagofga), no semestre 2026/2.

O objetivo principal do trabalho é implementar, comparar e analisar empiricamente diferentes estratégias de busca não informada, busca informada e busca local. A avaliação abrange sobre representação de estados, estruturas de dados, funções de custo e de avaliação, heurísticas, critérios de expansão e interpretação dos resultados de execução.

# Especificação do Problema

## Parte 1 — Busca em Ambiente Ponderado

Na Parte 1, um agente deve navegar em um ambiente bidimensional representado por uma grade retangular. O objetivo é encontrar um caminho válido entre o estado inicial ($S$) e o objetivo ($G$), contornando obstáculos (#) e minimizando o custo de travessia do terreno.

A movimentação é restrita a quatro direções (Norte, Leste, Sul, Oeste). O custo de cada ação é determinado exclusivamente pela célula de destino.

## Parte 2 — Problema das 8 Rainhas

Na Parte 2, aborda-se o problema clássico de posicionar 8 rainhas em um tabuleiro de xadrez de dimensão $8 \times 8$ de modo que nenhuma rainha ataque outra (ou seja, que não compartilhem a mesma linha, coluna ou diagonal).


# Estrutura do Projeto

## Organização dos Arquivos

```text
│
├── data/
│   └── mapa_teste.txt
├── src/
│   ├── parte1/
│   │   ├── algorithms.py
│   │   ├── heuristics.py
│   │   └── environment.py
│   └── parte2/
│       ├── hill_climbing.py
│       └── queens.py
├── tests/
│   └── test_cases.py
├── results/
│   └── experiment_results.csv
├── IA_USAGE.md
├── README.md
├── requirements.txt
└── run_experiments.py

```

---- 
----


## Entrega no SIGAA e repositório Git

O desenvolvimento deve ser mantido em um repositório Git acessível ao professor. O repositório deve permanecer **privado até o encerramento da correção**, com acesso concedido ao professor.

### 08/10/2026 - Parte 1

No SIGAA, envie um arquivo `.zip` com a versão executável da Parte 1. Antes da entrega, crie no repositório a tag:

```bash
git tag entrega-parte1
git push origin entrega-parte1
```

O `README.md` da entrega deve informar o endereço do repositório e a tag `entrega-parte1`. Não é necessário entregar o relatório final nesta etapa.

### 15/10/2026 - Entrega final

No SIGAA, envie:

- o relatório final em PDF;
- um arquivo `.zip` com o projeto completo.

Antes da entrega, crie no repositório a tag:

```bash
git tag entrega-final
git push origin entrega-final
```

O `README.md` e o relatório final devem informar o endereço do repositório e a tag `entrega-final`. A versão avaliada será a versão marcada por essa tag. Commits posteriores não substituem a versão entregue.

O histórico de commits poderá ser utilizado como elemento auxiliar na verificação da autoria e da contribuição dos integrantes, sem exigência de quantidade mínima de commits.

## Conteúdo deste pacote

```text
.
├── EC_IA_Trabalho_01_2026.pdf   # enunciado oficial
├── README.md                     # orientações gerais
├── IA_USAGE.md                   # registro do uso de IA
├── instrucoes_relatorio.md       # orientações para o relatório
├── .gitignore
├── requirements.txt
├── data/
│   └── mapa_teste.txt
├── src/
│   ├── __init__.py
│   ├── problem.py
│   ├── models.py
│   ├── heuristics.py
│   ├── search.py
│   ├── eight_queens.py
│   ├── hill_climbing.py
│   └── main.py
├── scripts/
│   └── run_experiments.py
├── tests/
│   └── test_problem.py
└── modelo_relatorio/
    ├── relatorio_sbc.tex
    └── sbc-template.sty
```

O fonte LaTeX do enunciado e os arquivos institucionais utilizados para sua composição não fazem parte do material de trabalho dos alunos.

## Parte 1 - Busca não informada e informada

Devem ser implementados:

- Busca em Largura - BFS;
- Busca em Profundidade - DFS;
- Busca de Custo Uniforme - UCS;
- Busca Gulosa;
- A*;
- heurísticas Manhattan e Euclidiana.

O mapa público está em `data/mapa_teste.txt`. O programa também será avaliado com mapas não disponibilizados previamente.

Exemplo de execução após a implementação:

```bash
python -m src.main busca --map data/mapa_teste.txt --algorithm astar --heuristic manhattan
```

## Parte 2 - Busca local

Devem ser implementados para o problema das 8 Rainhas:

- Hill Climbing;
- Random-Restart Hill Climbing.

Exemplos:

```bash
python -m src.main rainhas --algorithm hill --seed 42
python -m src.main rainhas --algorithm restart --seed 42 --max-restarts 50
```

## Teste inicial do código-base

Antes de implementar os algoritmos, execute:

```bash
python -m unittest discover -s tests -v
```

Os testes fornecidos verificam apenas a infraestrutura inicial. A equipe deve adicionar os casos de teste exigidos no enunciado.

## Experimentos

O arquivo `scripts/run_experiments.py` é um esqueleto para a execução padronizada dos experimentos utilizados no relatório. Ele deve ser completado pela equipe.

## Relatório

Consulte `instrucoes_relatorio.md` e a pasta `modelo_relatorio/`.

O relatório deve usar o modelo SBC fornecido, sem capa separada, respeitando o limite e os requisitos definidos no enunciado.

## Uso de Inteligência Artificial

Todo uso de ferramentas de IA deve obedecer à política descrita no enunciado e ser registrado em `IA_USAGE.md`.

## Observação importante

As funções correspondentes aos algoritmos e às heurísticas estão deliberadamente incompletas. O código fornecido é apenas a infraestrutura inicial do trabalho e não contém o gabarito das implementações.
