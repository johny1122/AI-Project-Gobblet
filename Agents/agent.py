import abc
from state import State
from action import Action


class Agent:

    @abc.abstractmethod
    def get_action(self, state: State) -> Action:
        raise NotImplemented

    @abc.abstractmethod
    def get_name(self) -> str:
        raise NotImplemented
