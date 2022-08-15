from agent import Agent
from state import State
from action import Action
import random


class RandomAgent(Agent):
    """
    performs random actions
    """

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()
        return random.choice(legal_actions)
