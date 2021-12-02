#   Make a decorator that wraps around a function and takes all the arguments and sigfigizes them
from typing import Callable


class SigFig:

    #   Allocate (??? correct word) variables here.
    __slots__ = "ea_sports_its_in_the_game"

    @staticmethod
    def sigfigize(func: Callable, indexes: list[int]):

        def wrapper(*args, **kwargs):

            real_args = list(args)

            for index in indexes:

                if type(args[index]) is str or type(args[index]) is float:

                    real_args[index] = SigFig(args[index])

            func (real_args, kwargs)

        return wrapper


