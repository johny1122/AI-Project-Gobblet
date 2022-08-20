import sys
from state import State
from cell import Cell
from globals import *
from typing import List
from location import Location





def corners_heuristic(state: State) -> int:
    score = 0
    player_color = state.player_turn

    first_importance = [state.board.left_diagonal, state.board.right_diagonal,
                        [Location(0, 0), Location(0, 1), Location(0, 2)],
                        [Location(0, 0), Location(1, 0), Location(2, 0)],
                        [Location(2, 0), Location(2, 1), Location(2, 2)],
                        [Location(0, 2), Location(1, 2), Location(2, 2)]]


    second_importance = [[Location(0, 1), Location(1, 1), Location(2, 1)],
                         [Location(1, 0), Location(1, 1), Location(1, 2)]]


    result = state.board.is_finished()
    if result:  # a player won or draw

        # draw
        if result == DRAW:
            score += 0
        # has winner
        elif result[1] == player_color:
            score += sys.maxsize
        elif result[1] != player_color:
            score -= sys.maxsize

    else:  # game not finished
        for line in first_importance:
            score += get_score_for_line(player_color, line, state, 20)
        for line in second_importance:
            score += get_score_for_line(player_color, line, state, 5)


    return score

#TODO: combine second and first importance score functions and give a
# different coefficient to multiply


def get_score_for_line(player_color: str, line: List[Cell], state:
State, coefficient: int) -> \
        int:
    score = 0
    for location in line:
        cell = state.board.get_cell(location)
        if cell.is_empty():
            score += 5
        elif cell.top().color == player_color:
            score += cell.top().size * coefficient
            if is_middle(location):
                score = score+500
            if is_corner(location= cell.location):
                # score = score*2
                score = score + 250

        elif cell.top().color != player_color:
            score -= cell.top().size * coefficient
            if is_middle(location):
                score = score - 500
            if is_corner(location= cell.location):
                score = score -250
                # if score < 0:
                #     score = score*2
                # else:
                #     score = score/2

    return score

# def get_score_for_first_importance(player_color: str, line: List[Cell], state:
# State) -> \
#         int:nt:
#
#     score = 0
#     for location in line:
#         cell = state.board.get_cell(location)
#         if cell.is_empty():
#             score += 5
#         elif cell.top().color == player_color:
#             score += cell.top().size * 20
#             if is_middle(location):
#                 score = score+500
#             if is_corner(location= cell.location):
#                 # score = score*2
#                 score = score + 250
#
#         elif cell.top().color != player_color:
#             score -= cell.top().size * 20
#             if is_middle(location):
#                 score = score - 500
#             if is_corner(location= cell.location):
#                 score = score -250
#                 # if score < 0:
#                 #     score = score*2
#                 # else:
#                 #     score = score/2
#
#     return score


# def get_score_for_second_importance(player_color: str, line: List[Cell], state:
# State) -> \
#         int:
#     score = 0
#     for location in line:
#         cell = state.board.get_cell(location)
#         if cell.is_empty():
#             score += 5
#         elif cell.top().color == player_color:
#             score += cell.top().size * 5
#             if is_middle(location):
#                 score = score + 500
#             if is_corner(location=cell.location):
#                 score = score +250
#
#         elif cell.top().color != player_color:
#             score -= cell.top().size * 5
#             if is_middle(location):
#                 score = score - 500
#             if is_corner(location=cell.location):
#                 score = score - 250
#                 # if score < 0:
#                 #     score = score * 2
#                 # else:
#                 #     score = score / 2
#
#     return score

def is_corner(location: Location) -> bool:
    if location.row == 0 and location.col == 0:
        return True
    elif location.row == 2 and location.col == 0:
        return True
    elif location.row == 0 and location.col == 2:
        return True
    elif location.row == 2 and location.col == 2:
        return True
    return False


def is_middle(location: Location) -> bool:
    if location.row == 1 and location.col == 1:
        return True
    return False