from typing import Union
from action import Action
from board import Board
from globals import *


class State:
    def __init__(self, player_turn: str, board: Union[Board, None] = None):
        self.board = Board() if board is None else board.deep_copy()
        self.player_turn = player_turn

    def get_legal_actions(self):
        legal_actions = []

        return legal_actions
        # TODO

    def generate_successor(self, action: Action, player_turn: str):
        # TODO
        pass

    def is_terminal(self):
        # TODO
        # return self._uttt.has_winner() or self._uttt.is_board_full()
        pass

    def deep_copy(self):
        new_state = State(self.board, self.player_turn)
        return new_state

    # def __str__(self):
    #     return str(self._uttt) + str(self.player_turn)
    #
    # def __hash__(self):
    #     return hash(str(self))
    #
    # def __eq__(self, other):
    #     return str(self) == str(other)
