import sys
from state import State
from cell import Cell
from globals import *
from typing import List
import Location



first_importance = [Board.left_diagonal, Board.right_diagonal,
                    [Location(0,0), Location(0,1), Location(0,2)],
                    [Location(0,0), Location(1,0), Location(2,0)],
                    [Location(2,0), Location(2,1), Location(2,2)],
                    [Location(0,2), Location(1,2), Location(2,2)]]

second_importance = Board.rows - first_importance

rows = [[Location(i, j) for j in range(ROW_COL_LENGTH)] for i in
        range(ROW_COL_LENGTH)]

def corners_heuristic(state: State) -> int:
    score = 0
    player_color = state.player_turn

    result = state.board.is_finished()
    if result:  # a player won or draw

        # draw
        if result == DRAW:
            score += 0
        # has winner
        elif result[1] == player_color:
            score += sys.maxsize
            # print (player_color)
            # print(score)
        elif result[1] != player_color:
            score -= sys.maxsize

    else:  # game not finished
        for line in first_importance:###############
            score += get_score_for_first_importance(player_color, line, state)
        for line in second_importance:
            score += get_score_for_second_importance(player_color, line, state)



    return score


def get_score_for_first_importance(player_color: str, line: List[Cell], state:
State) -> \
        int:
    score = 0
    for location in line:
        cell = state.board.get_cell(location)
        if cell.is_empty():
            score += 5
        if cell.top().color == player_color:
            score += cell.top().size * 10
            if is_corner(location= cell.location):
                score = score*2

        if cell.top().color != player_color:
            score -= cell.top().size * 10
            if is_corner(location= cell.location):
                if score < 0:
                    score = score*2
                else:
                    score = score/2

    return score


def get_score_for_second_importance(player_color: str, line: List[Cell], state:
State) -> \
        int:
    score = 0
    for location in line:
        cell = state.board.get_cell(location)
        if cell.is_empty():
            score += 2
        if cell.top().color == player_color:
            score += cell.top().size * 5
            if is_corner(location=cell.location):
                score = score * 2

        if cell.top().color != player_color:
            score -= cell.top().size * 5
            if is_corner(location=cell.location):
                if score < 0:
                    score = score * 2
                else:
                    score = score / 2

    return score

def is_corner(location: Location) -> bool:
    if location[0] == 0 and location[1] == 0:
        return True
    elif location[0] == 2 and location[1] == 0:
        return True
    elif location[0] == 0 and location[1] == 2:
        return True
    elif location[0] == 2 and location[1] == 2:
        return True
    return False
