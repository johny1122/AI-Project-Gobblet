from typing import Union, List
from action import Action
from Board import Board
from copy import deepcopy
from globals import *


class State:
    def __init__(self, player_turn: str, board: Union[Board, None] = None):
        self.board = Board() if board is None else deepcopy(board)
        self.player_turn = player_turn

    def get_legal_actions(self) -> List[Action]:
        return self.board.get_legal_actions(self.player_turn)

    def apply_action(self, action: Action):
        self.board.apply_action(action)

    def generate_successor(self, action: Action):  # assume action is legal
        if self.player_turn == BLUE:
            child_state = State(RED, self.board)
        else:
            child_state = State(BLUE, self.board)

        child_state.apply_action(action)
        return child_state

    def is_terminal(self) -> bool:
        if self.board.is_finished():
            return True
        return False

    def deep_copy(self):
        new_state = State(self.player_turn, self.board)
        return new_state

    # def __str__(self):
    #     return str(self._uttt) + str(self.player_turn)
    #
    # def __hash__(self):
    #     return hash(str(self))
    #
    # def __eq__(self, other):
    #     return str(self) == str(other)
