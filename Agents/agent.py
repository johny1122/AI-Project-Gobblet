import abc
import math
from globals import *
from state import *


class Agent:

    @abc.abstractmethod
    def get_action(self, state):
        raise NotImplemented
