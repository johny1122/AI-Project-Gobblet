import sys
import gui
import argparse
import time
import threading
from itertools import combinations
from Board import Board
from globals import *
from state import State
from action import Action

# Agents
from Agents.random_agent import RandomAgent
from Agents.reflex_agent import ReflexAgent
from Agents.human_agent import HumanAgent
from Agents.minimax_alpha_beta_agent import MinimaxAlpaBetaAgent

# Heuristics
from Heuristics.general_heuristic import general_heuristic


class Analyzer:
    def __init__(self):
        self.data = {color: {TOTAL_ACTIONS: 0,
                             TOTAL_TIME: 0.0,
                             AVG_ACTION_TIME: 0.0} for color in COLORS}

    def measure_action_time(self, player_turn: str, agent, state: State) -> Action:
        start_time = time.time()
        new_action = agent.get_action(state)
        end_time = time.time()
        self.data[player_turn][TOTAL_TIME] += (end_time - start_time)
        self.data[player_turn][TOTAL_ACTIONS] += 1
        return new_action

    def calculate_avg_time(self) -> None:
        self.data[BLUE][AVG_ACTION_TIME] = self.data[BLUE][TOTAL_TIME] / self.data[BLUE][TOTAL_ACTIONS]
        self.data[RED][AVG_ACTION_TIME] = self.data[RED][TOTAL_TIME] / self.data[RED][TOTAL_ACTIONS]

    def get_total_actions(self) -> int:
        return self.data[BLUE][TOTAL_ACTIONS] + self.data[RED][TOTAL_ACTIONS]


def run_all_matches(agents_list, iterations: int, show_display: bool):
    agents = []
    for agent in agents_list:
        if agent == RANDOM:
            agents.append(RandomAgent())
        elif agent == REFLEX:
            agents.append(ReflexAgent())
        elif agent == MINIMAX_GENERAL:
            agents.append(
                MinimaxAlpaBetaAgent(heuristic=general_heuristic, depth=2, name=MINIMAX_GENERAL,
                                     with_random=False))
        elif agent == MINIMAX_DEV_GENERAL:
            agents.append(
                MinimaxAlpaBetaAgent(heuristic=general_heuristic, depth=1, name=MINIMAX_DEV_GENERAL,
                                     with_random=True))
        # TODO: add more agents

    agents_matches = combinations(agents, 2)
    for agent1, agent2 in agents_matches:
        print(f'{Style.HEADER}===== {agent1.get_name()} vs {agent2.get_name()} ====={Style.ENDC}')
        run_match(agent1, agent2, iterations, show_display)


def run_match(agent1, agent2, iterations: int, show_display: bool):
    results = {color: {WINS: 0, AVG_ACTION_TIME: 0} for color in COLORS}
    results[DRAW] = 0
    for match in range(iterations):
        analyzer, winner = play(agent1, agent2, show_display)
        analyzer.calculate_avg_time()
        results[BLUE][AVG_ACTION_TIME] += analyzer.data[BLUE][AVG_ACTION_TIME]
        results[RED][AVG_ACTION_TIME] += analyzer.data[RED][AVG_ACTION_TIME]

        if winner is not None:
            if winner == agent1.get_name():
                results[BLUE][WINS] += 1
            elif winner == agent2.get_name():
                results[RED][WINS] += 1
        else:
            results[DRAW] += 1
    print_results(agent1.get_name(), agent2.get_name(), results, iterations)


def play(agent1, agent2, show_display: bool = False):
    board_game = Board()
    player_turn = BLUE
    curr_player = agent1
    opponent = agent2
    analyzer = Analyzer()
    state = State(player_turn, board_game)

    while not state.is_terminal():
        new_action = analyzer.measure_action_time(player_turn, curr_player, state)

        if show_display:
            gui.apply_action(new_action, state.board)

        state = state.generate_successor(new_action)

        # switch turns
        player_turn = change_turn(player_turn)
        curr_player, opponent = opponent, curr_player

    game_result = state.board.is_finished()
    winner = None
    if type(game_result) == tuple:  # found winner
        winner = game_result[1]  # winner color
        if winner == BLUE:
            winner = agent1.get_name()
        else:
            winner = agent2.get_name()
        if show_display:
            gui.markWinner(game_result[2][0], game_result[2][1], game_result[2][2])
        else:
            if game_result[1] == BLUE:
                print(
                    f'{agent1.get_name()} vs {agent2.get_name()}: {winner} Won! '
                    f'({Style.OKBLUE}{game_result[1]}{Style.ENDC})  total actions: {analyzer.get_total_actions()}')
            elif game_result[1] == RED:
                print(
                    f'{agent1.get_name()} vs {agent2.get_name()}: {winner} Won! '
                    f'({Style.FAIL}{game_result[1]}{Style.ENDC})  total actions: {analyzer.get_total_actions()}')

    elif game_result == DRAW:  # Draw
        if show_display:
            # TODO - display a tie
            pass
        else:
            print(f'{agent1.get_name()} vs {agent2.get_name()}: Draw!')

    return analyzer, winner


def print_results(agent1: str, agent2: str, results, iterations: int) -> None:
    print('------- Results -------')
    # print(f'Agent {agent1} vs {agent2}: ')
    for color, agent in zip(COLORS, [agent1, agent2]):
        print(
            f'{agent} wins:\t{results[color][WINS]}\t{(results[color][WINS] * HUNDRED_FLOAT) / iterations}%\t'
            f' avg_action:\t'
            f'{round(((results[color][AVG_ACTION_TIME] * SECONDS_TO_MILLISECONDS) / iterations), 3)} ms')

    print(f'draws:\t{(results[DRAW] * HUNDRED_FLOAT) / iterations}\n')


def change_turn(player_turn: str) -> str:
    if player_turn == BLUE:
        return RED
    return BLUE


##########################################################
# def manual_move(is_outside: bool, index: int, color: str = None) -> None:
#     global src_piece, dest_piece, clicks_count, board_game
#
#     piece = None
#     row, col = None, None
#     if is_outside:
#         stack_index = index
#         if color == BLUE:  # blue
#             piece = board_game.stacks[BLUE][stack_index].top()
#         elif color == RED:  # red
#             piece = board_game.stacks[RED][stack_index].top()
#
#     else:  # inside
#         cell_index = index
#         row, col = int(cell_index / 3), (cell_index % 3)
#         piece_location = Location(row, col)
#         piece = board_game.get_cell(piece_location).top()
#
#     if clicks_count == 1:
#         src_piece = piece
#         clicks_count += 1
#
#     elif clicks_count == 2:
#         if src_piece is not None and (row is not None and col is not None):
#             dest_piece = piece
#             new_action = Action(src_piece, src_piece.location, Location(row, col))
#
#             if board_game.is_action_legal(new_action):
#                 gui.apply_action(new_action, board_game)
#                 board_game.apply_action(new_action)
#                 turn_result = board_game.is_finished()
#                 if type(turn_result) == tuple:  # found winner
#                     gui.markWinner(turn_result[2][0], turn_result[2][1], turn_result[2][2])
#                     # TODO: stop game
#                 elif turn_result == DRAW:  # Draw
#                     # TODO - display a tie
#                     # TODO: stop game
#                     pass
#
#         clicks_count = 1
#         src_piece = None
#         dest_piece = None
##########################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--display', help='Add this argument to show GUI', nargs='?', const=True)
    parser.add_argument('--iterations', help='Number of rounds between two agents', type=int, default=1)
    parser.add_argument('--agents',
                        help=f'List of agents to run each one against the others: {ALL_AGENTS}',
                        nargs='+',
                        default=[], type=str)
    args = parser.parse_args()

    agents_list = args.agents
    show_display = args.display
    iterations = args.iterations

    if len(agents_list) == 1:
        print(
            f'Got only one agent. Need at least 2 different. Available agents: {ALL_AGENTS} '
            f'(look at globals.py for explanations)',
            file=sys.stderr)
        exit(1)

    # show_display = True  # TODO - delete
    if show_display:
        if len(agents_list) == 2:
            # play_thread = threading.Thread(target=play, args=[
            #     MinimaxAlpaBetaAgent(heuristic=general_heuristic, depth=1, name=MINIMAX_GENERAL,
            #                          with_random=False), RandomAgent(), True])
            play_thread = threading.Thread(target=play, args=[
                MinimaxAlpaBetaAgent(offensive_heuristic, depth=1,
                                     with_random=False), HumanAgent(), True])
            window_thread = threading.Thread(target=gui.buildBoard)
            play_thread.start()
            window_thread.start()
        else:
            print(f'Should display game only of a game of 2 agents. got {len(agents_list)}', file=sys.stderr)

    else:  # run without display
        agents_without_human = ALL_AGENTS
        agents_without_human.remove(HUMAN)
        if HUMAN in agents_list:
            print(f'Can\'t run Human agent without display. Available agents: {agents_without_human} '
                  f'(look at globals.py for explanations)',
                  file=sys.stderr)
            exit(1)

        run_all_matches(agents_list, iterations, show_display)
