from typing import List, Tuple, Union
from cell import Cell
from piece import Piece
from pieces_stack import PiecesStack
from location import Location
from action import Action
from globals import *
from copy import *


class Board:
    left_diagonal = [Location(i, i) for i in range(ROW_COL_LENGTH)]
    right_diagonal = [Location(i, 2 - i) for i in range(ROW_COL_LENGTH)]
    rows = [[Location(i, j) for j in range(ROW_COL_LENGTH)] for i in range(ROW_COL_LENGTH)]
    columns = [[Location(i, j) for i in range(ROW_COL_LENGTH)] for j in range(ROW_COL_LENGTH)]
    lines = [left_diagonal, right_diagonal] + rows + columns

    def __init__(self):
        self.stacks = {color: [] for color in COLORS}
        self.cells = []

        # create stacks
        for color in COLORS:
            for stack_index in range(STACKS_NUM):
                stack = PiecesStack()
                for size in SIZES:
                    stack.add(Piece(size, color, stack_index))
                self.stacks[color].append(stack)

        # create cells
        for row_index in range(ROW_COL_LENGTH):
            row = []
            for col_index in range(ROW_COL_LENGTH):
                row.append(Cell(PiecesStack(), Location(row_index, col_index)))
            self.cells.append(row)

    def get_cell(self, location: Location) -> Union[None, Cell]:
        if location.is_outside():
            return None
        return self.cells[location.row][location.col]

    def get_possible_pieces_outside(self, color: str) -> List[Piece]:
        if color == BLUE:
            stacks = self.stacks[BLUE]
        elif color == RED:
            stacks = self.stacks[RED]

        possible_outsides = []
        for stack in stacks:
            if stack.top() is not None:
                possible_outsides.append(stack.top())

        return possible_outsides

    def get_possible_pieces_inside(self, color: str) -> List[Piece]:
        inside_pieces = []
        for row in self.cells:
            for cell in row:
                if cell.color() == color:
                    if cell.top() is not None:
                        inside_pieces.append(cell.top())

        return inside_pieces

    def get_available_pieces(self, color: str) -> List[Piece]:
        return self.get_possible_pieces_outside(color) + self.get_possible_pieces_inside(color)

    def count_colors_in_line(self, line: List[Location]) -> Tuple[int, int]:
        blues, reds = 0, 0
        for location in line:
            color = self.cells[location.row][location.col].color()
            if color == BLUE:
                blues += 1
            elif color == RED:  # red
                reds += 1

        return blues, reds

    def found_winner(self) -> Union[Tuple[bool, str, List[Location]], bool]:
        for line in self.lines:

            blues, reds = self.count_colors_in_line(line)
            # print("blues ",blues,"   reds ",reds)
            if blues == ROW_COL_LENGTH:
                return True, BLUE, line
            elif reds == ROW_COL_LENGTH:
                return True, RED, line

        return False

    # TODO: maybe add to Cell for not calculating each time
    def lines_of_cell(self, cell: Cell) -> List[List[Location]]:
        lines = [line for line in self.lines if cell.location in line]
        return lines

    def is_action_legal(self, action: Action) -> bool:
        src_cell = self.get_cell(action.src)
        dest_cell = self.get_cell(action.dest)
        piece_to_move = action.piece

        if src_cell is None:  # src is outside (None means outside)
            outside_stack = self.stacks[action.piece.color][action.piece.stack_index]
            if len(outside_stack.pieces) == 0:  # src stack
                return False

        elif src_cell.is_empty():  # src is inside and empty
            return False

        if dest_cell.location.is_outside():
            return False

        if dest_cell.is_empty():  # dest is empty
            return True

        is_src_outside = (src_cell is None)
        # dest is not empty
        if dest_cell.top().size < piece_to_move.size:  # dest size smaller than piece_to_move
            if not is_src_outside:  # src is inside board
                return True

            else:  # src is outside board
                # check there are 2 opponent pieces in one of dest_cell's lines
                lines_of_dest_cell = self.lines_of_cell(dest_cell)
                for line in lines_of_dest_cell:
                    blues, reds = self.count_colors_in_line(line)
                    if piece_to_move.color == BLUE:
                        if reds == ROW_COL_LENGTH - 1:
                            return True
                    elif piece_to_move.color == RED:
                        if blues == ROW_COL_LENGTH - 1:
                            return True
        return False

    def get_actions_of_piece(self, piece: Piece) -> List[Action]:
        possible_actions = []
        for row in self.cells:
            for cell in row:
                new_action = Action(piece, piece.location, cell.location)
                if self.is_action_legal(new_action):
                    possible_actions.append(new_action)

        return possible_actions

    def get_legal_actions(self, color: str) -> List[Action]:
        all_possible_pieces = self.get_available_pieces(color)
        legal_actions = []
        for piece in all_possible_pieces:
            legal_actions.extend(self.get_actions_of_piece(piece))

        return legal_actions

    def is_draw(self):  # draw is when board is full
        for row in self.cells:
            for cell in row:
                if cell.is_empty():
                    return False
        return True

    def is_finished(self):
        turn_result = self.found_winner()
        if type(turn_result) == tuple:
            return turn_result

        elif self.is_draw():
            return DRAW

        return False

    def apply_action(self, action: Action) -> None:
        piece = action.piece
        src = action.src
        dest = action.dest

        # add piece to new location
        piece_copy = deepcopy(piece)
        self.cells[dest.row][dest.col].add(piece_copy)
        self.cells[dest.row][dest.col].top().location = dest

        # remove piece from src stack
        if src.is_outside():
            self.cells[dest.row][dest.col].top().stack_index = NONE
            self.stacks[piece.color][piece.stack_index].pop()

        # remove piece from src cell
        else:
            self.cells[src.row][src.col].pop()
