import sys
import gui
import argparse
import time
import threading
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
from Heuristics.corners_heuristic import corners_heuristic
from Heuristics.aggressive_heuristic import aggressive_heuristic


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


def get_agent(agent_name: str):
    if agent_name == RANDOM:
        return RandomAgent()
    elif agent_name == REFLEX:
        return ReflexAgent()
    elif agent_name == HUMAN:
        return HumanAgent()
    elif agent_name == MINIMAX_GENERAL:
        return MinimaxAlpaBetaAgent(heuristic=general_heuristic, depth=SEARCH_DEPTH,
                                    name=MINIMAX_GENERAL,
                                    with_random=False)
    elif agent_name == MINIMAX_DEV_GENERAL:
        return MinimaxAlpaBetaAgent(heuristic=general_heuristic, depth=SEARCH_DEPTH,
                                    name=MINIMAX_DEV_GENERAL,
                                    with_random=True)
    elif agent_name == MINIMAX_CORNERS:
        return MinimaxAlpaBetaAgent(heuristic=corners_heuristic, depth=SEARCH_DEPTH,
                                    name=MINIMAX_CORNERS,
                                    with_random=False)
    elif agent_name == MINIMAX_DEV_CORNERS:
        return MinimaxAlpaBetaAgent(heuristic=corners_heuristic, depth=SEARCH_DEPTH,
                                    name=MINIMAX_DEV_CORNERS,
                                    with_random=True)
    elif agent_name == MINIMAX_AGGRESSIVE:
        return MinimaxAlpaBetaAgent(heuristic=aggressive_heuristic, depth=SEARCH_DEPTH,
                                    name=MINIMAX_AGGRESSIVE,
                                    with_random=False)
    elif agent_name == MINIMAX_DEV_AGGRESSIVE:
        return MinimaxAlpaBetaAgent(heuristic=aggressive_heuristic, depth=SEARCH_DEPTH,
                                    name=MINIMAX_DEV_AGGRESSIVE,
                                    with_random=True)


def run_all_matches(agents_list, iterations: int, show_display: bool):
    if agents_list == [ALL]:
        agents_list = ALL_AGENTS_WITHOUT_HUMAN

    for agent1_name in agents_list:
        for agent2_name in agents_list:
            if agent1_name != agent2_name:
                print(f'{Style.HEADER}===== {agent1_name} vs {agent2_name} ====={Style.ENDC}')
                run_match(agent1_name, agent2_name, iterations, show_display)


def run_match(agent1_name, agent2_name, iterations: int, show_display: bool):
    results = {color: {WINS: 0, AVG_ACTION_TIME: 0} for color in COLORS}
    results[DRAW] = 0
    results[TOTAL_ACTIONS] = 0
    for match in range(iterations):
        agent1 = get_agent(agent1_name)
        agent2 = get_agent(agent2_name)
        analyzer, winner = play(agent1, agent2, show_display)
        analyzer.calculate_avg_time()
        results[BLUE][AVG_ACTION_TIME] += analyzer.data[BLUE][AVG_ACTION_TIME]
        results[RED][AVG_ACTION_TIME] += analyzer.data[RED][AVG_ACTION_TIME]
        results[TOTAL_ACTIONS] += analyzer.get_total_actions()

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
    turns = 0

    while not state.is_terminal():
        if turns == MAX_TURNS_ALLOWED:
            break
        turns += 1
        new_action = analyzer.measure_action_time(player_turn, curr_player, state)

        if show_display:
            gui.queue.append((new_action, state.board))

        state = state.generate_successor(new_action)

        # switch turns
        player_turn = change_turn(player_turn)
        curr_player, opponent = opponent, curr_player

    if turns == MAX_TURNS_ALLOWED:
        game_result = DRAW
    else:
        game_result = state.board.is_finished()
    winner = None
    if type(game_result) == tuple:  # found winner
        winner = game_result[1]  # winner color
        if winner == BLUE:
            winner = agent1.get_name()
        else:
            winner = agent2.get_name()
        if show_display:
            gui.queue.append((None, state.board))

    elif game_result == DRAW:  # Draw
        print(f'{agent1.get_name()} vs {agent2.get_name()}: Draw!')

    return analyzer, winner


def print_results(agent1: str, agent2: str, results, iterations: int) -> None:
    print('------- Results -------')
    for color, agent in zip(COLORS, [agent1, agent2]):
        print(
            f'{agent} wins: {results[color][WINS]}\t{(results[color][WINS] * HUNDRED_FLOAT) / iterations}%\t'
            f' avg_action_time:\t'
            f'{round(((results[color][AVG_ACTION_TIME] * SECONDS_TO_MILLISECONDS) / iterations), 3)} ms\t'
            f'avg_actions:\t{results[TOTAL_ACTIONS] / iterations}')

    print(f'draws:\t{(results[DRAW] * HUNDRED_FLOAT) / iterations}\n')


def change_turn(player_turn: str) -> str:
    if player_turn == BLUE:
        return RED
    return BLUE


if __name__ == '__main__':
    if len(sys.argv) == 1:  # no args entered
        print(USAGE_HELP)
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('--display', help='Add this argument to show GUI (only works with 2 agents)',
                        nargs='?', const=True)
    parser.add_argument('--iterations', help='Number of rounds between each two agents', type=int, default=1)
    parser.add_argument('--agents',
                        help=f'List of agents to run each one against the others: {ALL_AGENTS}',
                        nargs='+',
                        default=[], type=str)
    args = parser.parse_args()

    agents_list = args.agents
    show_display = args.display
    iterations = args.iterations

    if (len(agents_list) == 1) and (agents_list[0] != ALL):
        print(
            f'Got only one agent. Need at least 2 different. Available agents: {ALL_AGENTS} '
            f'(look at globals.py for explanations)',
            file=sys.stderr)
        exit(1)

    if len(agents_list) > 1 and ALL in agents_list:
        print(
            f'ALL must be entered alone', file=sys.stderr)
        exit(1)

    if show_display:
        if len(agents_list) == 2:
            if iterations != 1:
                print(f'Only one game is played when display is selected', file=sys.stderr)
            agent1 = get_agent(agents_list[0])
            agent2 = get_agent(agents_list[1])
            play_thread = threading.Thread(target=play, args=[agent1, agent2, True])
            window_thread = threading.Thread(target=gui.buildBoard)
            play_thread.start()
            window_thread.start()

        else:
            print(f'Display game is only available in a game of 2 agents. got {len(agents_list)}',
                  file=sys.stderr)

    else:  # run without display
        if HUMAN in agents_list:
            print(f'Can\'t run Human agent without display. Available agents: {ALL_AGENTS_WITHOUT_HUMAN} '
                  f'(look at globals.py for explanations)',
                  file=sys.stderr)
            exit(1)

        run_all_matches(agents_list, iterations, show_display)
