from typing import Callable
from project1.token import Token


class RejectException(Exception):
    pass


class AcceptException(Exception):
    pass


StateTransitionFunction = Callable[[str], "StateTransitionFunction"]
TokenFactory = Callable[[str, int], Token]


class FiniteStateMachine:
    __slots__ = ["_initial_state", "_token_factory"]

    def __init__(
        self, initial_state: StateTransitionFunction, token_factory: TokenFactory
    ) -> None:
        self._initial_state = initial_state
        self._token_factory = token_factory

    def run(self, input_string: str, line_num: int) -> tuple[int, Token]:
        current_state = self._initial_state
        number_of_chars = len(input_string)
        for i in range(0, number_of_chars + 1):
            char_at_i: str = input_string[i] if i < number_of_chars else ""
            try:
                current_state = current_state(char_at_i)
            except AcceptException:
                return (i, self._token_factory(input_string[:i], line_num))
            except RejectException:
                break
        return (0, self._token_factory("", line_num))

    def token(self, value: str) -> Token:
        raise NotImplementedError

    @staticmethod
    def accept(input_char: str) -> StateTransitionFunction:
        raise AcceptException

    @staticmethod
    def reject(input_char: str) -> StateTransitionFunction:
        raise RejectException
