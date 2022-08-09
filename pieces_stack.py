from typing import Union, List
from piece import Piece


class PiecesStack:

    def __init__(self, pieces=Union[None, List[Piece]]):
        if pieces is None:
            self.pieces = []
        else:
            self.pieces = pieces

    def is_empty(self) -> bool:
        if not self.pieces:
            return True
        else:
            return False

    def add(self, piece: Piece) -> bool:
        if self.is_add_valid(piece):
            self.pieces.append(piece)
            return True
        return False

    def pop(self) -> None:
        if not self.is_empty():
            self.pieces.pop()

    def top(self) -> Union[None, Piece]:
        if not self.is_empty():
            return self.pieces[-1]
        return None

    def is_add_valid(self, piece: Piece) -> bool:
        top_piece = self.top()
        if top_piece is None:
            return True
        if piece.size > top_piece.size:
            return True
        return False
