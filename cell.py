from typing import Union
from piece import Piece
from pieces_stack import PiecesStack
from location import Location
from globals import *


class Cell:
    def __init__(self, stack: PiecesStack = PiecesStack(), location: Location = Location(OUTSIDE, OUTSIDE)):
        self.stack = stack
        self.location = location

    def is_empty(self) -> bool:
        return self.stack.is_empty()

    def top(self) -> Union[None, Piece]:
        return self.stack.top()

    def color(self) -> Union[str, None]:
        if self.is_empty():
            return None
        return self.stack.top().color

    def add(self, piece: Piece) -> bool:
        return self.stack.add(piece)  # return True if succeeded and False otherwise

    def pop(self):
        self.stack.pop()
