from location import Location
from piece import Piece


class Action:
    def __init__(self, piece: Piece, source: Location, destination: Location):
        self.piece = piece
        self.src = source
        self.dest = destination
