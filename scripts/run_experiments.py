import argparse
import math
import statistics
import sys
import time
from pathlib import Path
from random import Random
from typing import Callable, Optional, Tuple

from src.eight_queens import initial_board, render
from src.heuristics import euclidean, manhattan
from src.hill_climbing import hill_climbing, random_restart
from src.problem import WeightedGrid
from src.search import astar, bfs, dfs, greedy, ucs

Pos = Tuple[int, int]

# Dicionarios CLI
ALGORITHMS = {
    "bfs": bfs,
    "dfs": dfs,
    "uniform_cost": ucs,
    "greedy": greedy,
    "astar": astar,
}

HEURISTICS = {
    "manhattan": manhattan,
    "euclidean": euclidean,
}


def run_single_search(map_path: Path, algorithm_name: str, heuristic_name: Optional[str] = None) -> None:
    if not map_path.exists():
        print(f"Erro: O arquivo de mapa '{map_path}' nao foi encontrado")
        sys.exit(1)

    grid = WeightedGrid.from_file(map_path)
    func = ALGORITHMS[algorithm_name]

    if algorithm_name in {"greedy", "astar"}:
        if not heuristic_name:
            print(f"Erro: O algoritmo '{algorithm_name}' requer uma --heuristic")
            sys.exit(1)
        heur_func = HEURISTICS[heuristic_name]
        res = func(grid, heur_func)
    else:
        res = func(grid)

    print(f"Algoritmo: {algorithm_name.upper()}")
    if heuristic_name:
        print(f"Heuristica: {heuristic_name.capitalize()}")
    print(f"Mapa: {map_path}")
    print("-" * 50)
    print(f"Sucesso: {res.found}")
    print(f"Passos (Acoes): {res.steps}")
    print(f"Custo Total: {res.cost}")
    print(f"Estados Gerados: {res.generated}")
    print(f"Estados Expandidos: {res.expanded}")
    print(f"Pico Fronteira: {res.peak_frontier}")
    print(f"Pico Estados Armazenados: {res.peak_stored_states}")

    if res.found:
        print("\nCaminho Visual:")
        print(grid.render_path(res.path))


# Bateria de experimentos no mapa especifico
def run_part1(map_path: Path) -> None:
    if not map_path.exists():
        print(f"Erro: O arquivo de mapa '{map_path}' nao foi encontrado.")
        return

    grid = WeightedGrid.from_file(map_path)

    # Nome, Funcao de Busca, Funcao Heuristica
    configs = [
        ("BFS", bfs, None),
        ("DFS", dfs, None),
        ("UCS", ucs, None),
        ("Gulosa", greedy, manhattan),
        ("A*", astar, manhattan),
        ("Gulosa", greedy, euclidean),
        ("A*", astar, euclidean),
    ]

    # Cabecalho da tabela de resultados
    print(
        f"{'Alg.':<10} | {'Heur.':<12} | {'Passos':<6} | {'Custo':<6} | "
        f"{'Ger.':<6} | {'Exp.':<6} | {'Pico F.':<7} | {'Pico Mem.':<9} | {'Tempo(ms)'}"
    )
    print("-" * 100)

    for name, func, heur in configs:
        if heur:
            res = func(grid, heur)
            heur_name = "Manhattan" if heur == manhattan else "Euclidiana"
        else:
            res = func(grid)
            heur_name = "-"

        # Loop de execucoes para calcular a mediana do tempo de execucao
        times = []
        for _ in range(30):
            start = time.perf_counter()
            if heur:
                func(grid, heur)
            else:
                func(grid)
            end = time.perf_counter()
            times.append((end - start) * 1000)

        median_time = statistics.median(times)

        if res.found:
            print(
                f"{name:<10} | {heur_name:<12} | {res.steps:<6} | {res.cost:<6.1f} | "
                f"{res.generated:<6} | {res.expanded:<6} | {res.peak_frontier:<7} | "
                f"{res.peak_stored_states:<9} | {median_time:.2f}"
            )
        else:
            print(
                f"{name:<10} | {heur_name:<12} | {'FALHA':<6} | {'-':<6} | "
                f"{res.generated:<6} | {res.expanded:<6} | {res.peak_frontier:<7} | "
                f"{res.peak_stored_states:<9} | {median_time:.2f}"
            )

# Bateria de experimentos - 8 rainhas
def run_part2() -> None:
    "Experimento 8 rainhas"


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", help="Subcomandos disponiveis")

    # Subcomando 'busca' 
    busca_parser = subparsers.add_parser("busca", help="Executa um algoritmo de busca especifico em um mapa")
    busca_parser.add_argument("--map", type=Path, required=True, help="Caminho do arquivo de mapa")
    busca_parser.add_argument("--algorithm", type=str, required=True, choices=list(ALGORITHMS.keys()), help="Algoritmo de busca a ser executado",)
    busca_parser.add_argument("--heuristic", type=str, choices=list(HEURISTICS.keys()), help="Funcao heuristica",)

    # Subcomando 'experimentos' para rodar a bateria de testes do relatório
    exp_parser = subparsers.add_parser("experimentos", help="Roda a bateria completa de experimentos")
    exp_parser.add_argument("--map", type=Path, default=Path("data/mapa_teste.txt"), help="Caminho do mapa público")

    args = parser.parse_args()

    if args.command == "busca":
        run_single_search(args.map, args.algorithm, args.heuristic)
    elif args.command == "experimentos":
        run_part1(args.map)
        run_part2()
    else:
        # Se nenhum parâmetro for fornecido, roda os experimentos padrao
        default_map = Path("data/mapa_teste.txt")
        run_part1(default_map)
        #run_part2()


if __name__ == "__main__":
    main()


#####