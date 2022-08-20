import random
import sys
from Agents.agent import Agent
from globals import *
from state import State
from action import Action


class MinimaxAlpaBetaAgent(Agent):
    """
    MiniMax agent with alpha-beta pruning
    """

    def __init__(self, heuristic, depth: int, name: str, with_random: bool):
        self.evaluation_function = heuristic
        self.depth = depth
        self.with_random = with_random
        self.random_value = 3
        self.name = name
        if with_random:
            self.name += f'_{heuristic.__name__}'

    def alpha_beta_recursion(self, curr_depth, agent_turn, curr_state: State, alpha, beta):
        if curr_depth == 0:  # reached a leaf  or  finished game
            return self.evaluation_function(curr_state)

        if agent_turn == MAX:
            actions_list = []
            children_scores = []
            max_score = -sys.maxsize
            # count = 0
            for legal_action in curr_state.get_legal_actions():
                # count += 1
                child_state = curr_state.generate_successor(legal_action)
                curr_score = self.alpha_beta_recursion(curr_depth, MIN, child_state, alpha, beta)
                # print(f'player: {curr_state.player_turn}     curr_score: {curr_score}')
                max_score = max(max_score, curr_score)
                alpha = max(alpha, curr_score)
                if beta <= alpha:
                    break
                actions_list.append(legal_action)
                children_scores.append(curr_score)

            if curr_depth == self.depth:  # root  ->  return action and not score
                # print('====================================')
                # print(f'count1: {count}')
                # print(f'actions_list: {len(actions_list)}       children_scores: {len(children_scores)}')
                # print(f'max_score: {max_score}')
                # print(f'children_scores: {children_scores}')
                #
                highest_scores_indexes = [i for i, score in enumerate(children_scores) if score == max_score]

                # print(f'highest_scores_indexes: {highest_scores_indexes}')
                random_highest_index = random.choice(highest_scores_indexes)
                # print(f'random_highest_index: {random_highest_index}')
                # print('====================================')
                return actions_list[random_highest_index]  # return the best action to do now

            return max_score  # not root  ->  return max score

        else:  # MIN
            min_score = sys.maxsize
            count = 0
            for legal_action in curr_state.get_legal_actions():
                count += 1
                child_state = curr_state.generate_successor(legal_action)
                curr_score = self.alpha_beta_recursion(curr_depth - 1, MAX, child_state, alpha, beta)
                min_score = min(min_score, curr_score)
                beta = min(beta, curr_score)
                if beta <= alpha:
                    break
            # print(f'count2: {count}')
            return min_score

    def minimax_recursion(self, curr_depth, agent_turn, curr_state: State):
        if curr_depth == 0:  # reached a leaf
            return self.evaluation_function(curr_state)

        children_scores = []
        actions_list = []
        for legal_action in curr_state.get_legal_actions():
            child_state = curr_state.generate_successor(legal_action)
            if agent_turn == MAX:
                children_scores.append(self.minimax_recursion(curr_depth, MIN, child_state))
            else:  # MIN
                children_scores.append(self.minimax_recursion(curr_depth - 1, MAX, child_state))
            actions_list.append(legal_action)
        # print(children_scores)

        if agent_turn == MAX:
            if curr_depth == self.depth:  # root  ->  return action and not score
                max_score = max(children_scores)
                max_score_index = children_scores.index(max_score)
                return actions_list[max_score_index]  # return the best action to do now

            return max(children_scores, default=0)  # not root
            # ->  return
            # max score

        else:  # MIN
            return min(children_scores, default=0)

    def get_action(self, state) -> Action:
        if self.with_random:
            if random.random() < (5.0 / (self.random_value ** 2)):
                self.random_value += 0.1
                return random.choice(state.get_legal_actions())
        return self.alpha_beta_recursion(self.depth, MAX, state, -sys.maxsize,
                                         sys.maxsize)

    def get_name(self) -> str:
        return self.name
