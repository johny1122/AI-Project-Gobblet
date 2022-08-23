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

    def alpha_beta_recursion(self, curr_depth, agent_turn, curr_state: State, alpha, beta):
        if curr_depth == 0:  # reached a leaf  or  finished game
            return self.evaluation_function(curr_state)

        if agent_turn == MAX:
            for legal_action in curr_state.get_legal_actions():
                child_state = curr_state.generate_successor(legal_action)
                curr_score = self.alpha_beta_recursion(curr_depth - 1, MIN, child_state, alpha, beta)
                if beta <= alpha:
                    break
                alpha = max(alpha, curr_score)
            return alpha

        else:  # MIN
            for legal_action in curr_state.get_legal_actions():
                child_state = curr_state.generate_successor(legal_action)
                curr_score = self.alpha_beta_recursion(curr_depth - 1, MAX, child_state, alpha, beta)
                if beta <= alpha:
                    break
                beta = min(beta, curr_score)
            return beta

    def get_action(self, state: State) -> Action:
        if self.with_random:
            self.random_value += 0.8
            if random.random() < (3.5 / (self.random_value ** 2)):
                return random.choice(state.get_legal_actions())

        actions_scores = []
        for legal_action in state.get_legal_actions():
            child_state = state.generate_successor(legal_action)
            score = self.alpha_beta_recursion(self.depth - 1, MIN, child_state, alpha=-sys.maxsize,
                                              beta=sys.maxsize)
            actions_scores.append((legal_action, score))
        just_scores = [score for _, score in actions_scores]
        best_score = max(just_scores)
        best_actions = [action for action, score in actions_scores if score == best_score]
        return random.choice(best_actions)

    def get_name(self) -> str:
        return self.name
