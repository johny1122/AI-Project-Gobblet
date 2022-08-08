import random
from agent import *


class MinimaxAlpaBetaAgent(Agent):
    """
    MiniMax agent with alpha-beta pruning
    """

    def __init__(self, heuristic, depth):
        self.evaluation_function = heuristic
        self.depth = depth

    def alpha_beta_recursion(self, curr_depth, agent_turn, curr_state: State, alpha, beta):
        if curr_depth == 0 or curr_state.done:  # reached a leaf  or  has no legal actions
            return self.evaluation_function(curr_state)

        if agent_turn == MAX:
            actions_list = []
            children_scores = []
            max_score = 0
            for legal_action in curr_state.get_legal_actions(agent_turn):
                child_state = curr_state.generate_successor(agent_index=agent_turn, action=legal_action)
                curr_score = self.alpha_beta_recursion(curr_depth, MIN, child_state, alpha, beta)
                max_score = max(max_score, curr_score)
                alpha = max(alpha, curr_score)
                if beta <= alpha:
                    break
                actions_list.append(legal_action)
                children_scores.append(curr_score)

            if curr_depth == self.depth:  # root  ->  return action and not score
                highest_scores_indexes = [i for i, score in enumerate(children_scores) if score == max_score]
                random_highest_index = children_scores[random.choice(highest_scores_indexes)]
                return actions_list[random_highest_index]  # return the best action to do now

            return max_score  # not root  ->  return max score

        else:  # MIN
            min_score = math.inf
            for legal_action in curr_state.get_legal_actions(agent_turn):
                child_state = curr_state.generate_successor(agent_index=agent_turn, action=legal_action)
                curr_score = self.alpha_beta_recursion(curr_depth - 1, MAX, child_state, alpha, beta)
                min_score = min(min_score, curr_score)
                beta = min(beta, curr_score)
                if beta <= alpha:
                    break

            return min_score

    def get_action(self, state):
        return self.alpha_beta_recursion(self.depth, MAX, state, -math.inf, math.inf)
