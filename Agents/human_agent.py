from agent import Agent


class HumanAgent(Agent):
    """
    human controlled agent
    """

    def get_action(self, state):
        legal_moves = state.get_legal_actions()
        while True:
            human_action = ui.get_input()
            if human_action in legal_moves:
                return human_action
            else:
                # show human message the "action is invalid and try again"
                pass

        # TODO