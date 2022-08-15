import abc
import math
from globals import *
from state import State
from action import Action


class Agent:

    @abc.abstractmethod
    def get_action(self, state: State) -> Action:
        raise NotImplemented
