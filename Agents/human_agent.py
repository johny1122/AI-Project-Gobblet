from agent import Agent
from state import State
from action import Action


class HumanAgent(Agent):
    """
    human controlled agent
    """

    def get_action(self, state: State) -> Action:
        legal_actions = state.get_legal_actions()
        while True:
            human_action = ui.get_input()
            if human_action in legal_actions:
                return human_action
            else:
                # show human message the "action is invalid and try again"
                pass

        # TODO