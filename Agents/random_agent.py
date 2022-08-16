from Agents.agent import Agent
from state import State
from action import Action
from globals import *
import random


class RandomAgent(Agent):
    """
    performs random actions
    """

    def __init__(self):
        self.name = RANDOM

    def get_name(self) -> str:
        return self.name

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()
        return random.choice(legal_actions)
