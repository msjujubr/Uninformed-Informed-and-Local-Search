from src.heuristics import euclidean, manhattan
from src.models import SearchResult
from src.problem import Pos, WeightedGrid

from collections import deque
from collections.abc import Callable
import heapq

Heuristic = Callable[[tuple[int, int], tuple[int, int]], float]

# Reconstroi o caminho e a lista de acoes
# A partir do mapeamento de antecessores.
def retomada_caminho(parent: dict, start: Pos, goal: Pos) -> tuple[list[Pos], list[str]]:
    path = []
    actions = []
    obj = goal
    while obj != start:
        path.append(obj)
        prev, act = parent[obj]
        actions.append(act)
        obj = prev
    path.append(start)
    path.reverse()
    actions.reverse()
    return path, actions

# Retorna o custo total do caminho
def custo(problem: WeightedGrid, path: list[Pos]) -> float:
    return float(sum(problem.step_cost(pos) for pos in path[1:]))


# Busca Não Informada: Busca em Largura
def bfs(problem: WeightedGrid) -> SearchResult:
    start = problem.start
    frontier = deque([start])
    visited = {start}
    parent = {start: None}

    generated = 1
    expanded = 0
    peak_frontier = 1
    peak_stored_states = 1

    while frontier:
        obj = frontier.popleft()

        # Se o objetivo for reconhecido ao ser retirado da fronteira, não é expandido
        if problem.goal_test(obj):
            path, actions = retomada_caminho(parent, start, obj)
            cost = custo(problem, path)
            return SearchResult(found=True, algorithm="bfs", path=path,
                                actions=actions, cost=cost, generated=generated,
                                expanded=expanded, peak_frontier=peak_frontier,
                                peak_stored_states=peak_stored_states, )

        expanded += 1
        for action, nxt, _ in problem.successors(obj):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (obj, action)
                frontier.append(nxt)
                generated += 1
                peak_frontier = max(peak_frontier, len(frontier))
                peak_stored_states = max(peak_stored_states, len(visited))


    return SearchResult(found=False, algorithm="bfs", generated=generated,
                        expanded=expanded, peak_frontier=peak_frontier,
                        peak_stored_states=peak_stored_states, )


# Busca Não Informada: Busca em Profundidade
def dfs(problem: WeightedGrid) -> SearchResult:
    start = problem.start
    frontier = [start]
    visited = {start}
    parent = {start: None}

    generated = 1
    expanded = 0
    peak_frontier = 1
    peak_stored_states = 1

    while frontier:
        obj = frontier.pop()

        if problem.goal_test(obj):
            path, actions = retomada_caminho(parent, start, obj)
            cost = custo(problem, path)
            return SearchResult(found=True, algorithm="dfs", path=path,
                                actions=actions, cost=cost, generated=generated,
                                expanded=expanded, peak_frontier=peak_frontier,
                                peak_stored_states=peak_stored_states, )


        expanded += 1
        succs = list(problem.successors(obj))
        # Para ordem N -> L -> S -> O em pilha (LIFO), inverte: O, S, L, N
        for action, nxt, _ in reversed(succs):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (obj, action)
                frontier.append(nxt)
                generated += 1
                peak_frontier = max(peak_frontier, len(frontier))
                peak_stored_states = max(peak_stored_states, len(visited))

    return SearchResult(found=False, algorithm="dfs", generated=generated,
                        expanded=expanded, peak_frontier=peak_frontier,
                        peak_stored_states=peak_stored_states, )


# Busca Não Informada: Busca de Custo Uniforme
def ucs(problem: WeightedGrid) -> SearchResult:
    start = problem.start
    insert_counter = 0

    heap = [(0, insert_counter, start)]
    g_cost = {start: 0}
    parent = {start: None}
    explored = set()

    generated = 1
    expanded = 0
    peak_frontier = 1
    peak_stored_states = 1

    while heap:
        g_val, _, obj = heapq.heappop(heap)

        # Se o custo retirado da fila for maior que o melhor custo registrado 
        # para esse no, significa que ja encontramos um caminho melhor e esta 
        # entrada ficou obsoleta
        if g_val > g_cost[obj]:
            continue

        if problem.goal_test(obj):
            path, actions = retomada_caminho(parent, start, obj)
            return SearchResult(found=True, algorithm="ucs", path=path,
                                actions=actions, cost=float(g_val), generated=generated,
                                expanded=expanded, peak_frontier=peak_frontier,
                                peak_stored_states=peak_stored_states, )


        expanded += 1
        explored.add(obj)

        for action, nxt, step_cost in problem.successors(obj):
            new_g = g_val + step_cost
            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                parent[nxt] = (obj, action)
                insert_counter += 1
                heapq.heappush(heap, (new_g, insert_counter, nxt))
                generated += 1

                frontier_states = {p for _, _, p in heap}
                peak_frontier = max(peak_frontier, len(frontier_states))
                peak_stored_states = max(
                    peak_stored_states, len(frontier_states | explored)
                )

    return SearchResult(found=False, algorithm="ucs", generated=generated,
                        expanded=expanded, peak_frontier=peak_frontier,
                        peak_stored_states=peak_stored_states, )


# Busca Informada: Busca Gulosa - busca pelo melhor primeiro
def greedy(problem: WeightedGrid, heuristic: Heuristic) -> SearchResult:
    start = problem.start
    goal = problem.goal
    insert_counter = 0

    h_start = heuristic(start, goal)
    heap = [(h_start, insert_counter, start)]
    parent = {start: None}
    visited = {start}

    generated = 1
    expanded = 0
    peak_frontier = 1
    peak_stored_states = 1

    while heap:
        _, _, obj = heapq.heappop(heap)

        if problem.goal_test(obj):
            path, actions = retomada_caminho(parent, start, obj)
            cost = custo(problem, path)
            return SearchResult(found=True, algorithm="gulosa", path=path,
                                actions=actions, cost=cost, generated=generated,
                                expanded=expanded, peak_frontier=peak_frontier,
                                peak_stored_states=peak_stored_states, )

        expanded += 1

        for action, nxt, _ in problem.successors(obj):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (obj, action)
                h_nxt = heuristic(nxt, goal)
                insert_counter += 1
                heapq.heappush(heap, (h_nxt, insert_counter, nxt))
                generated += 1

                frontier_states = {p for _, _, p in heap}
                peak_frontier = max(peak_frontier, len(frontier_states))
                peak_stored_states = max(peak_stored_states, len(visited))

    return SearchResult(found=False, algorithm="greedy", generated=generated,
                    expanded=expanded, peak_frontier=peak_frontier,
                    peak_stored_states=peak_stored_states, )



# Busca Informada: Busca A*
def astar(problem: WeightedGrid, heuristic: Heuristic) -> SearchResult:
    start = problem.start
    goal = problem.goal
    insert_counter = 0

    # Força os custos como float para evitar inconsistências de tipo
    g_cost = {start: 0.0}
    h_start = float(heuristic(start, goal))
    f_start = h_start

    # (f(n), h(n), g(n), id_insercao, estado)
    heap = [(f_start, h_start, 0.0, insert_counter, start)]
    parent = {start: None}
    explored = set()

    generated = 1
    expanded = 0
    peak_frontier = 1
    peak_stored_states = 1

    while heap:
        f_val, h_val, g_val, _, obj = heapq.heappop(heap)

        # Trata imprecisao decimal no float com margem de tolerancia (1e-9)
        if g_val > g_cost[obj] + 1e-9:
            continue

        if problem.goal_test(obj):
            path, actions = retomada_caminho(parent, start, obj)
            return SearchResult(found=True, algorithm="astar", path=path,
                                actions=actions, cost=float(g_cost[obj]), generated=generated,
                                expanded=expanded, peak_frontier=peak_frontier,
                                peak_stored_states=peak_stored_states, )


        expanded += 1
        explored.add(obj)

        for action, nxt, step_cost in problem.successors(obj):
            new_g = float(g_cost[obj] + step_cost)
            
            # Se for um caminho melhor
            if nxt not in g_cost or new_g < g_cost[nxt] - 1e-9:
                g_cost[nxt] = new_g
                parent[nxt] = (obj, action)
                h_nxt = float(heuristic(nxt, goal))
                f_nxt = new_g + h_nxt
                insert_counter += 1

                heapq.heappush(heap, (f_nxt, h_nxt, new_g, insert_counter, nxt))
                generated += 1

                frontier_states = {p for _, _, _, _, p in heap}
                peak_frontier = max(peak_frontier, len(frontier_states))
                peak_stored_states = max(
                    peak_stored_states, len(frontier_states | explored)
                )

    return SearchResult(found=False, algorithm="astar", generated=generated,
                    expanded=expanded, peak_frontier=peak_frontier,
                    peak_stored_states=peak_stored_states, )