from location import Location
from globals import *


class Piece:
    def __init__(self, size: int, color: str):
        self.size = size
        self.color = color
        self.location = Location(row=OUTSIDE, col=OUTSIDE)
