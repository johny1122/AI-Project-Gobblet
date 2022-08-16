from Agents.agent import Agent
from state import State
from action import Action
from globals import *


class ReflexAgent(Agent):
    """
    performs actions based solely on the current situation
    chooses always the first legal action
    """

    def __init__(self):
        self.name = REFLEX

    def get_name(self) -> str:
        return self.name

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()
        return legal_actions[0]
