from location import Location
from piece import Piece


class Action:
    def __init__(self, piece: Piece, source: Location, destination: Location):
        self.piece = piece
        self.src = source
        self.dest = destination

    def __eq__(self, other):
        return (self.piece == other.piece) and (self.src == other.src) and (self.dest == other.dest)
