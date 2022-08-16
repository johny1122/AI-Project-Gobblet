import gui
from Agents.agent import Agent
from state import State
from action import Action
from location import Location
from time import sleep
from globals import *


class HumanAgent(Agent):
    """
    human controlled agent
    """

    def __init__(self):
        self.name = HUMAN

    def get_name(self) -> str:
        return self.name

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()

        while True:
            src_tuple, dest_tuple = gui.get_clicks()
            if src_tuple is None or dest_tuple is None:
                continue
            src_is_outside, src_index, src_color = src_tuple
            dest_is_outside, dest_index, dest_color = dest_tuple

            # create src piece
            src_piece = None
            piece_location = Location(OUTSIDE, OUTSIDE)
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

            if src_piece is None:
                continue

            if dest_is_outside:
                continue

            else:  # inside
                cell_index = dest_index
                row, col = int(cell_index / 3), (cell_index % 3)

            new_action = Action(src_piece, piece_location, Location(row, col))
            if new_action in legal_actions:
                return new_action
            sleep(0.5)
