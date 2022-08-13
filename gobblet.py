from gui import *
from piece import Piece
from action import Action
from Board import Board
import argparse



def manual_move(piece: Piece):
    global src_piece, dest_piece, clicks_count
    clicks_count += 1

    if clicks_count == 1:
        src_piece = piece

    elif clicks_count == 2:
        dest_piece = piece
        new_action = Action(src_piece, src_piece.location, dest_piece.location)
        # if



def main(show_display):
    board_game = Board()
    if show_display:
        build_main_window()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--display', help='Add this argument to show GUI',
                        nargs='?', const=True)

    args = parser.parse_args()

    clicks_count = 0
    src_piece = None
    dest_piece = None

    main(args.display)