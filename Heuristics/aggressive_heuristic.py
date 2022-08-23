import sys
from state import State


def aggressive_heuristic(state: State) -> int:
    player, opponent = 0, 0
    player_color = state.player_turn
    result = state.board.is_finished()
    if result:  # a player won or draw
        # has winner
        if result[1] == player_color:
            return sys.maxsize
        elif result[1] != player_color:
            return -sys.maxsize

    else:
        player, opponent = 0, 0
        for line in state.board.cells:
            for cell in line:
                if not cell.is_empty():
                    if cell.top().color == state.player_turn:
                        player += cell.top().size
                    else:
                        opponent += cell.top().size

    return player - opponent
