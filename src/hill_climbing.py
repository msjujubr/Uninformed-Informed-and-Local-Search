from dataclasses import dataclass, field
from random import Random
from typing import List

from .eight_queens import Board, conflicts, moves, apply_move, initial_board


@dataclass
class HillResult:
    success: bool
    initial: Board
    final: Board
    initial_conflicts: int
    final_conflicts: int
    iterations: int
    evaluated_states: int
    restarts: int = 0
    history: List[int] = field(default_factory=list)


# Hill Climbing sem movimentos laterais
# Escolhe o primeiro melhor vizinho conforme a ordem de vizinhança
def hill_climbing(initial: Board) -> HillResult:
    at = initial.copy()
    at_h = conflicts(at)
    
    it = 0
    visitados = 1 # conta o estado atual
    hist = [at_h]

    while True:
        if at_h == 0: 
            return HillResult(
                success = True,
                initial = initial,
                final = at,
                initial_conflicts = hist[0],
                final_conflicts = at_h,
                iterations = it,
                evaluated_states = visitados,
                restarts = 0, 
                history = hist,
            )

        mov = None
        mov_h = at_h

        # Avalia vizinhos
        for m in moves(at):
            visitados += 1
            vizin = apply_move(at, m)
            h_val = conflicts(vizin)  # Corrigido aqui (=)

            # Escolhe o primeiro vizinho com menor valor de h
            if h_val < mov_h:
                mov_h = h_val
                mov = m
                
        if mov == None or mov_h >= at_h:
            return HillResult(
                success = (at_h == 0),
                initial = initial,
                final = at,
                initial_conflicts = hist[0],
                final_conflicts = at_h,
                iterations = it,
                evaluated_states = visitados,
                restarts = 0,
                history = hist,
            ) 
   
        at = apply_move(at, mov)  # Corrigido aqui (mov em vez de best_move)
        at_h = mov_h
        it += 1
        hist.append(at_h)


# Executa Hill Climbing com reinícios aleatórios até encontrar solução
# ou atingir max_restarts.
def random_restart(rng: Random, max_restarts: int = 50) -> HillResult:
   
    total_evaluated = 0
    total_iterations = 0
    restarts_count = 0
    
    # Primeira tentativa (restarts = 0)
    current_initial = initial_board(rng)
    result = hill_climbing(current_initial)
    
    total_evaluated += result.evaluated_states
    total_iterations += result.iterations
    
    if result.success:
        return HillResult(
            success=True,
            initial=result.initial,
            final=result.final,
            initial_conflicts=result.initial_conflicts,
            final_conflicts=result.final_conflicts,
            iterations=total_iterations,
            evaluated_states=total_evaluated,
            restarts=restarts_count,
            history=result.history,
        )
        
    while restarts_count < max_restarts:
        restarts_count += 1
        current_initial = initial_board(rng)
        next_result = hill_climbing(current_initial)
        
        total_evaluated += next_result.evaluated_states
        total_iterations += next_result.iterations
        
        if next_result.success:
            return HillResult(
                success=True,
                initial=next_result.initial,
                final=next_result.final,
                initial_conflicts=next_result.initial_conflicts,
                final_conflicts=next_result.final_conflicts,
                iterations=total_iterations,
                evaluated_states=total_evaluated,
                restarts=restarts_count,
                history=next_result.history,
            )
            
    # Se esgotar os reinícios sem sucesso
    return HillResult(
        success=False,
        initial=result.initial,
        final=next_result.final,
        initial_conflicts=result.initial_conflicts,
        final_conflicts=next_result.final_conflicts,
        iterations=total_iterations,
        evaluated_states=total_evaluated,
        restarts=restarts_count,
        history=next_result.history,
    )