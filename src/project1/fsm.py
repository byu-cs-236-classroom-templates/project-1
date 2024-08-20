from typing import Callable
from project1.token import Token


class AcceptException(Exception):
    pass


class RejectException(Exception):
    pass


StateTransitionFunction = Callable[[int, str], "State"]
State = tuple[int, StateTransitionFunction]


class FiniteStateMachine:
    __slots__ = ["_initial_state"]

    def __init__(self, initial_state: State) -> None:
        self._initial_state = initial_state

    def run(self, input_string: str) -> tuple[int, Token]:
        current_state: State = self._initial_state
        number_of_chars = len(input_string)
        for i in range(0, number_of_chars + 1):
            char_at_i: str = input_string[i] if i < number_of_chars else ""
            try:
                chars_read, transition = current_state
                current_state = transition(chars_read, char_at_i)
            except (AcceptException, RejectException):
                break
        chars_read, _ = current_state
        value = input_string[:chars_read]
        return (chars_read, self.token(value))

    def token(self, value: str) -> Token:
        return Token.undefined(value)

    @staticmethod
    def accept(chars_read: int, input_char: str) -> State:
        raise AcceptException

    @staticmethod
    def reject(chars_read: int, input_char: str) -> State:
        raise RejectException


class Colon(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__((0, Colon.s0))

    def token(self, value: str) -> Token:
        match value:
            case ":":
                return Token.colon(value)
            case _:
                return super().token(value)

    @staticmethod
    def s0(chars_read: int, char: str) -> State:
        if char == ":":
            return chars_read + 1, FiniteStateMachine.accept
        else:
            return 0, FiniteStateMachine.reject


class Eof(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__((0, Eof.s0))

    def token(self, value: str) -> Token:
        match value:
            case "":
                return Token.eof(value)
            case _:
                return super().token(value)

    @staticmethod
    def s0(chars_read: int, char: str) -> State:
        if char == "":
            return chars_read + 1, FiniteStateMachine.accept
        else:
            return 0, FiniteStateMachine.reject


class WhiteSpace(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__((0, WhiteSpace.s0))

    def token(self, value: str) -> Token:
        return Token.whitespace(value)

    @staticmethod
    def s0(chars_read: int, char: str) -> State:
        if char in [" ", "\t", "\r", "\n"]:
            return chars_read + 1, WhiteSpace.s1
        else:
            return 0, FiniteStateMachine.reject

    @staticmethod
    def s1(chars_read: int, char: str) -> State:
        if char in [" ", "\t", "\r", "\n"]:
            return chars_read + 1, WhiteSpace.s1
        else:
            return chars_read, FiniteStateMachine.accept
