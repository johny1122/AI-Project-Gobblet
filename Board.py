from typing import List, Tuple, Union
from cell import Cell
from piece import Piece
from pieces_stack import PiecesStack
from location import Location
from action import Action
from globals import *


class Board:
    left_diagonal = [Location(i, i) for i in range(ROW_COL_LENGTH)]
    right_diagonal = [Location(i, 2 - i) for i in range(ROW_COL_LENGTH)]
    rows = [[Location(i, j) for j in range(ROW_COL_LENGTH)] for i in range(ROW_COL_LENGTH)]
    columns = [[Location(i, j) for i in range(ROW_COL_LENGTH)] for j in range(ROW_COL_LENGTH)]
    lines = [left_diagonal, right_diagonal] + rows + columns

    def __init__(self):
        self.stacks = {color: [] for color in COLORS}
        for color in COLORS:
            for stack_index in range(STACKS_NUM):
                stack = PiecesStack()
                for size in SIZES:
                    stack.add(Piece(size, color, stack_index))
                self.stacks[color].append(stack)

        self.cells = []
        for row_index in range(ROW_COL_LENGTH):
            row = []
            for col_index in range(ROW_COL_LENGTH):
                row.append(Cell(PiecesStack(), Location(row_index, col_index)))
            self.cells.append(row)

    def get_cell(self, location: Location) -> Cell:
        return self.cells[location.row][location.col]

    def get_possible_pieces_outside(self, color: str) -> List[Piece]:
        if color == WHITE:
            stacks = self.stacks[WHITE]
        elif color == BLACK:
            stacks = self.stacks[BLACK]

        possible_outsides = []
        for stack in stacks:
            possible_outsides.append(stack.top())

        return possible_outsides

    def get_possible_pieces_inside(self, color: str) -> List[Piece]:
        inside_pieces = []
        for row in self.cells:
            for cell in row:
                if cell.color == color:
                    inside_pieces.append(cell.top())

        return inside_pieces

    def get_available_pieces(self, color: str) -> List[Piece]:
        return self.get_possible_pieces_outside(color) + self.get_possible_pieces_inside(color)

    def count_colors_in_line(self, line: List[Location]) -> Tuple[int, int]:
        whites, blacks = 0, 0
        for location in line:
            color = self.cells[location.row][location.col].color()
            if color == WHITE:
                whites += 1
            else:  # black
                blacks += 1

        return whites, blacks

    def found_winner(self) -> Union[Tuple[bool, str, List[Location]], bool]:
        for line in self.lines:
            whites, blacks = self.count_colors_in_line(line)
            if whites == ROW_COL_LENGTH:
                return True, WHITE, line
            elif blacks == ROW_COL_LENGTH:
                return True, BLACK, line

        return False

    # TODO: maybe add to Cell for not calculating each time
    def lines_of_cell(self, cell: Cell) -> List[List[Location]]:
        lines = [line for line in self.lines if cell.location in line]
        return lines

    def is_action_legal(self, action: Action) -> bool:
        src_cell = self.get_cell(action.src)
        dest_cell = self.get_cell(action.dest)
        piece_to_move = action.piece

        if dest_cell.is_empty():  # dest is empty
            return True

        # dest is not empty
        if dest_cell.top().size < piece_to_move.size:  # dest size smaller than piece_to_move
            if not src_cell.location.is_outside():  # src is inside board
                return True

            else:  # src is outside board
                # check there are 2 opponent pieces in one of dest_cell's lines
                lines_of_dest_cell = self.lines_of_cell(dest_cell)
                for line in lines_of_dest_cell:
                    whites, blacks = self.count_colors_in_line(line)
                    if piece_to_move.color == WHITE:
                        if blacks == ROW_COL_LENGTH - 1:
                            return True
                    elif piece_to_move.color == BLACK:
                        if whites == ROW_COL_LENGTH - 1:
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

    def apply_action(self, action: Action) -> None:
        piece = action.piece
        src = action.src
        dest = action.dest

        # add piece to new location
        self.cells[dest.row][dest.col].add(piece)
        self.cells[dest.row][dest.col].top().location = dest

        # remove piece from src stack
        if src.is_outside():
            self.cells[dest.row][dest.col].top().stack_index = NONE
            self.stacks[piece.color][piece.stack_index].pop()

        # remove piece from src cell
        else:
            self.cells[src.row][src.col].pop()
