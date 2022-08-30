import sys
from state import State
from cell import Cell
from globals import *
from typing import List


def general_heuristic(state: State) -> int:
    score = 0
    player_color = state.player_turn

    result = state.board.is_finished()
    if result:  # a player won
        # has winner
        if result[1] == player_color:
            return sys.maxsize
        elif result[1] != player_color:
            return -sys.maxsize

    else:  # game not finished
        for line in state.board.lines:
            blues, reds = state.board.count_colors_in_line(line)
            if reds == blues == 0:
                score += 0
            elif reds == 0:
                score += get_score_of_line_with_one_color(player_color, BLUE, line, state)
            elif blues == 0:
                score += get_score_of_line_with_one_color(player_color, RED, line, state)

            else:  # there are red and blues in line
                score += get_score_of_line_with_2_colors(player_color, line, state)

    return score


def get_score_of_line_with_one_color(player_color: str, line_color: str, line: List[Cell], state: State) -> int:
    score = 0
    for location in line:
        cell = state.board.get_cell(location)
        if cell.is_empty():
            score += 1
        else:
            score += (cell.top().size * 10)

    if player_color == line_color:
        return score
    return -score


def get_score_of_line_with_2_colors(player_color: str, line: List[Cell], state: State) -> int:
    score = 0
    min_opponent_size = LARGE
    for location in line:
        cell = state.board.get_cell(location)
        if not cell.is_empty():
            if cell.top().color != player_color and cell.top().size < min_opponent_size:
                min_opponent_size = cell.top().size

            if cell.top().color == player_color:
                score += cell.top().size * 10
            else:
                score -= cell.top().size * 10

    for stack in state.board.stacks[player_color]:
        if (not stack.is_empty()) and stack.top().size > min_opponent_size:
            return score
    return 0
