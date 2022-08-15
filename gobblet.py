import gui
from gui import *
from action import Action
from Board import Board
from location import Location
import argparse
from globals import *

board_game = Board()
clicks_count = 1


def main(show_display, agents, iterations):
    global board_game
    board_game = Board()
    if show_display:
        build_main_window()

    else:
        # create agents

        pass


def manual_move(is_outside: bool, index: int, color: str = None) -> None:
    global src_piece, dest_piece, clicks_count, board_game
    # TODO: check if the rule of adding from outside to row works!! (it doesnt..)

    piece = None
    row, col = None, None
    if is_outside:
        stack_index = index
        if color == BLUE:  # blue
            piece = board_game.stacks[BLUE][stack_index].top()
        elif color == RED:  # red
            piece = board_game.stacks[RED][stack_index].top()

    else:  # inside
        cell_index = index
        row, col = int(cell_index / 3), (cell_index % 3)
        piece_location = Location(row, col)
        piece = board_game.get_cell(piece_location).top()

    if clicks_count == 1:
        src_piece = piece
        clicks_count += 1

    elif clicks_count == 2:
        if src_piece is not None and (row is not None and col is not None):
            dest_piece = piece
            new_action = Action(src_piece, src_piece.location, Location(row, col))

            if board_game.is_action_legal(new_action):
                gui.apply_action(new_action, board_game)
                board_game.apply_action(new_action)
                turn_result = board_game.is_finished()
                if type(turn_result) == tuple:  # found winner
                    gui.markWinner(turn_result[2][0], turn_result[2][1], turn_result[2][2])
                    # TODO: stop game
                elif turn_result == DRAW:  # Draw
                    # TODO - display a tie
                    # TODO: stop game
                    pass

        clicks_count = 1
        src_piece = None
        dest_piece = None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--display', help='Add this argument to show GUI', nargs='?', const=True)
    parser.add_argument('--iterations', help='Number of rounds between two agents', type=int)
    parser.add_argument('--agents', help='List of agents to run each one against the others', nargs='+',
                        default=[], type=str)

    args = parser.parse_args()

    src_piece = None
    dest_piece = None

    agents_list = args.agents
    show_display = args.display
    iterations = args.iterations
    main(show_display, agents_list, iterations)
