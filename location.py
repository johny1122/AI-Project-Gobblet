from globals import *


class Location:

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def is_outside(self) -> bool:
        return self.row == OUTSIDE

    def __eq__(self, other) -> bool:
        return (self.row == other.row) and (self.col == other.col)

    def __repr__(self):
        return f'({self.row},{self.col})'
