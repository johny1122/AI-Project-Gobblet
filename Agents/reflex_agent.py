from agent import Agent
from state import State
from action import Action


class ReflexAgent(Agent):
    """
    performs actions based solely on the current situation
    chooses always the first legal action
    """

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()
        return legal_actions[0]
