from random import Random
from typing import Iterable, List, Tuple

Board = List[int]
Move = Tuple[int, int]  # (coluna, nova_linha)
N = 8


def initial_board(rng: Random) -> Board:
    """Geração padronizada: uma rainha aleatória por coluna."""
    return [rng.randrange(N) for _ in range(N)]


# Retorna o numero de pares nao ordenados de rainhas que se atacam
def conflicts(board: Board) -> int:
    cont = 0
    for c1 in range(N):
        r1 = board[c1]
        for c2 in range(c1+1, N):
            r2 = board[c2]
            if r1 == r2 or abs(r1 - r2) == abs(c1 - c2):
                # se estiverem na mesma linha/diagonal
                cont += 1
    return cont


# Gera a vizinhanca na ordem: 
# coluna 0..7; dentro de cada coluna, linha 0..7, exceto a linha atual.
def moves(board: Board) -> Iterable[Move]:
    for col in range(N):
        current_row = board[col]
        for row in range(N):
            if row != current_row:
                yield (col, row)



def apply_move(board: Board, move: Move) -> Board:
    col, row = move
    if not 0 <= col < N or not 0 <= row < N:
        raise ValueError("Movimento fora do tabuleiro.")
    new_board = board.copy()
    new_board[col] = row
    return new_board


def render(board: Board) -> str:
    rows = []
    for r in range(N):
        rows.append(" ".join("Q" if board[c] == r else "." for c in range(N)))
    return "\n".join(rows)
