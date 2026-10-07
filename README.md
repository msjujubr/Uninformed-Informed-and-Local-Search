# Busca Não Informada, Busca Informada e Busca Local

![Python](https://img.shields.io/badge/LANG-Python-green.svg)
![VSCode](https://img.shields.io/badge/IDE-VSCode-informational)
![ISO](https://img.shields.io/badge/ISO-Linux-blueviolet)

- **Aluno(a):** `Júlia de Moura Souza`
- **Repositório Git:** [`link do repositório`](https://github.com/msjujubr/Uninformed-Informed-and-Local-Search)
- **Tag:** `entrega-parte1`

  - **Parte 1 - Busca não informada e informada:** entrega em **08/10/2026**.
    
  - **Parte 2 - Busca local e entrega final:** entrega em **15/10/2026**.

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



## Parte 2 - Busca local

Devem ser implementados para o problema das 8 Rainhas:

Exemplos:

```bash
python -m scripts.run_experiments rainhas --algorithm hill --seed 42
python -m scripts.run_experiments rainhas --algorithm restart --seed 42 --max-restarts 50
```

## Teste inicial do código-base

Antes de implementar os algoritmos, execute:

```bash
python -m unittest discover -s tests -v
```


---
---
---
---
---

## Orientações de Execução e Observações do Projeto
> **Importante:** Sempre execute os comandos a partir da **raiz do projeto** (onde estão os diretórios `src/`, `data/`, `scripts/`, etc.).

### 1. Bateria Completa de Experimentos da Parte 1 (`run_part1`)

A execução dos experimentos da Parte 1 roda todos os algoritmos de busca (BFS, DFS, UCS, Gulosa e A*) com suas respectivas heurísticas no mapa informado, coletando métricas como passos, custo, nós gerados/expandidos e tempo de execução.

#### Modo Padrão (Sem parâmetros)
Executa a bateria de testes utilizando o mapa padrão `data/mapa_teste.txt`:

```bash
python -m scripts.run_experiments
```

#### Modo Explícito (`experimentos`)
Executa especificamente a suíte de experimentos:

```bash
python -m scripts.run_experiments experimentos
```

#### Especificando um Mapa Alternativo
Para testar a bateria de experimentos em outro mapa:

```bash
python -m scripts.run_experiments experimentos --map data/outro_mapa.txt
```

---

### Execução de Algoritmo
Para executar um único algoritmo de busca e visualizar o caminho no mapa, utilize o subcomando `busca`:

* **A* com Heurística Manhattan:**
  ```bash
  python -m scripts.run_experiments busca --map data/mapa_teste.txt --algorithm astar --heuristic manhattan
  ```

* **Busca Gulosa com Heurística Euclidiana:**
  ```bash
  python -m scripts.run_experiments busca --map data/mapa_teste.txt --algorithm greedy --heuristic euclidean
  ```

* **Busca em Largura (BFS):**
  ```bash
  python -m scripts.run_experiments busca --map data/mapa_teste.txt --algorithm bfs
  ```

* **Busca em Profundidade (DFS):**
  ```bash
  python -m scripts.run_experiments busca --map data/mapa_teste.txt --algorithm dfs
  ```

* **Busca de Custo Uniforme (UCS):**
  ```bash
  python -m scripts.run_experiments busca --map data/mapa_teste.txt --algorithm uniform_cost
  ```

---