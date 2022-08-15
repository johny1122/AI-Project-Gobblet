import gui
from agent import Agent
from state import State
from action import Action
from location import Location
from globals import *


class HumanAgent(Agent):
    """
    human controlled agent
    """

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()

        while True:
            src_tuple, dest_tuple = gui.get_clicks()
            src_is_outside, src_index, src_color = src_tuple
            dest_is_outside, dest_index, dest_color = dest_tuple

            # create src piece
            src_piece = None
            if src_is_outside:
                stack_index = src_index
                if src_color == BLUE:  # blue
                    src_piece = state.board.stacks[BLUE][stack_index].top()
                elif src_color == RED:  # red
                    src_piece = state.board.stacks[RED][stack_index].top()

            else:  # inside
                cell_index = src_index
                row, col = int(cell_index / 3), (cell_index % 3)
                piece_location = Location(row, col)
                src_piece = state.board.get_cell(piece_location).top()

            # create dest piece
            dest_piece = None
            if dest_is_outside:
                stack_index = dest_index
                if dest_color == BLUE:  # blue
                    dest_piece = state.board.stacks[BLUE][stack_index].top()
                elif dest_color == RED:  # red
                    dest_piece = state.board.stacks[RED][stack_index].top()

            else:  # inside
                cell_index = dest_index
                row, col = int(cell_index / 3), (cell_index % 3)
                piece_location = Location(row, col)
                dest_piece = state.board.get_cell(piece_location).top()

            new_action = Action(src_piece, src_piece.location, dest_piece.location)
            if new_action in legal_actions:
                return new_action
