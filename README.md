# Busca Não Informada, Busca Informada e Busca Local

![Python](https://img.shields.io/badge/LANG-Python-green.svg)
![VSCode](https://img.shields.io/badge/IDE-VSCode-informational)
![ISO](https://img.shields.io/badge/ISO-Linux-blueviolet)

- **Aluno(a):** `Júlia de Moura Souza`
- **Repositório Git:** [`link do repositório`](https://github.com/msjujubr/Uninformed-Informed-and-Local-Search)
- **Tag:** `entrega-final`


<div align="center"> <table> <tr> <td>
 

Este projeto foi desenvolvido para a disciplina **Inteligência Artificial** do CEFET-MG (Campus Divinópolis), sob a orientação do [Prof. Tiago Alves de Oliveira](https://github.com/tiagofga), no semestre 2026/2.

O objetivo principal do trabalho é implementar, comparar e analisar empiricamente diferentes estratégias de busca não informada, busca informada e busca local. A avaliação abrange sobre representação de estados, estruturas de dados, funções de custo e de avaliação, heurísticas, critérios de expansão e interpretação dos resultados de execução.


### Parte 1 — Busca em Ambiente Ponderado
Na Parte 1, um agente deve navegar em um ambiente bidimensional representado por uma grade retangular. O objetivo é encontrar um caminho válido entre o estado inicial ($S$) e o objetivo ($G$), contornando obstáculos (#) e minimizando o custo de travessia do terreno.

A movimentação é restrita a quatro direções (Norte, Leste, Sul, Oeste). O custo de cada ação é determinado exclusivamente pela célula de destino.

São implementadas:
- Busca em Largura - BFS;
- Busca em Profundidade - DFS;
- Busca de Custo Uniforme - UCS;
- Busca Gulosa;
- A*;
- heurísticas Manhattan e Euclidiana.

### Parte 2 — Problema das 8 Rainhas

Na Parte 2, aborda-se o problema clássico de posicionar 8 rainhas em um tabuleiro de xadrez de dimensão $8 \times 8$ de modo que nenhuma rainha ataque outra (ou seja, que não compartilhem a mesma linha, coluna ou diagonal).
Serão implementadas:

- Hill Climbing;
- Random-Restart Hill Climbing.


# Estrutura do Projeto

## Organização dos Arquivos

```text
│
├── data/
│   └── mapa_teste.txt
├── docs/
|   ├── IA_USAGE.md
|   ├── relatorio_final.pdf
│   └── requirements.txt
├── scripts/
│   └── run_experiments.py
├── src/
│   ├── eight_queens.py
│   ├── heuristics.py
│   ├── hill_climbing.py
│   ├── main.py
│   ├── models.py
│   ├── problem.py
│   └── search.py
├── tests/
│   └── test_problem.py
├── results/
│   └── experiment_results.csv
├── .gitignore
└── README.md
```

## Teste inicial do código-base

Antes de implementar ou executar os algoritmos, certifique-se de que o ambiente está correto rodando os testes unitários:
Bash

```bash
python -m unittest discover -s tests -v
```

Sempre execute os comandos a partir da raiz do projeto (onde estão os diretórios src/, data/, scripts/, etc.).




## Parte 1 — Busca em Ambiente Ponderado (busca)

Para executar um único algoritmo de busca e visualizar o caminho no mapa:

A com Heurística Manhattan:*

```bash
    python -m src.main busca --map data/mapa_teste.txt --algorithm astar --heuristic manhattan
```

Busca Gulosa com Heurística Euclidiana:


```bash
    python -m src.main busca --map data/mapa_teste.txt --algorithm greedy --heuristic euclidean
```

Busca em Largura (BFS):

```bash
    python -m src.main busca --map data/mapa_teste.txt --algorithm bfs
```

Busca em Profundidade (DFS):

```bash
    python -m src.main busca --map data/mapa_teste.txt --algorithm dfs
```
    Busca de Custo Uniforme (UCS):
   
```bash
    python -m src.main busca --map data/mapa_teste.txt --algorithm uniform_cost
```

Caso opte por executar a bateria de testes:
```bash
python scripts/run_experiments.py experimentos
```


## 2. Parte 2 — Problema das 8 Rainhas (rainhas)

Para executar os algoritmos de busca local para o problema das 8 Rainhas:

Hill Climbing:

```bash
    python -m src.main rainhas --algorithm hill --seed 42
```

Random-Restart Hill Climbing:
```bash
    python -m src.main rainhas --algorithm restart --seed 42 --max-restarts 50
```




```bash
git tag entrega-final
git push origin entrega-final
```


---