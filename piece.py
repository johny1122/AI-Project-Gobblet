from location import Location
from globals import *


class Piece:
    def __init__(self, size: int, color: str, stack_index: int = NONE):
        self.size = size
        self.color = color
        self.location = Location(row=OUTSIDE, col=OUTSIDE)
        self.stack_index = stack_index

    def __eq__(self, other):
        return (self.size == other.size) and (self.color == other.color) and \
               (self.location == other.location) and (self.stack_index == other.stack_index)
