from typing import List, Tuple, Union
from cell import Cell
from piece import Piece
from pieces_stack import PiecesStack
from location import Location
from globals import *


class Board:
    rows = [[Location(i, j) for j in range(ROW_COL_LENGTH)] for i in range(ROW_COL_LENGTH)]
    columns = [[Location(i, j) for i in range(ROW_COL_LENGTH)] for j in range(ROW_COL_LENGTH)]
    left_diagonal = [Location(i, i) for i in range(ROW_COL_LENGTH)]
    right_diagonal = [Location(i, 2 - i) for i in range(ROW_COL_LENGTH)]
    lines = [left_diagonal, right_diagonal] + rows + columns

    def __init__(self):
        self.whites = [Piece(SMALL, WHITE), Piece(MEDIUM, WHITE), Piece(LARGE, WHITE)] * 3
        self.blacks = [Piece(SMALL, BLACK), Piece(MEDIUM, BLACK), Piece(LARGE, BLACK)] * 3

        self.stacks_white = [
            PiecesStack(self.whites[:3]),
            PiecesStack(self.whites[3:6]),
            PiecesStack(self.whites[6:])
        ]

        self.stacks_black = [
            PiecesStack(self.blacks[:3]),
            PiecesStack(self.blacks[3:6]),
            PiecesStack(self.blacks[6:])
        ]

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
            stacks = self.stacks_white
        else:
            stacks = self.stacks_black

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

    def get_possible_pieces(self, color: str) -> List[Piece]:
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
