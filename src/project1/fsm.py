from typing import Callable
from project1.token import Token


State = Callable[[int, str], "StateAndOutput"]
StateAndOutput = tuple[State, int]


def run_fsm(fsm: "FiniteStateMachine", input_string: str) -> tuple[int, Token]:
    current_state: State = fsm.initial_state
    next_state: State

    output_chars_read: int = 0

    input_chars_read: int = 0
    input_char: str = ""

    number_of_chars = len(input_string)
    for i in range(0, number_of_chars + 1):
        input_chars_read = output_chars_read
        input_char = input_string[i] if i < number_of_chars else ""

        next_state, output_chars_read = current_state(input_chars_read, input_char)
        if next_state in {
            FiniteStateMachine.s_accept,
            FiniteStateMachine.s_reject,
        }:
            break

        current_state = next_state

    value = input_string[:output_chars_read]
    return (output_chars_read, fsm.token(value))


class FiniteStateMachine:
    __slots__ = ["initial_state"]

    def __init__(self, initial_state: State) -> None:
        self.initial_state = initial_state

    def token(self, value: str) -> Token:
        return Token.undefined(value)

    @staticmethod
    def s_accept(input_chars_read: int, input_char: str) -> StateAndOutput:
        return FiniteStateMachine.s_accept, input_chars_read

    @staticmethod
    def s_reject(input_chars_read: int, input_char: str) -> StateAndOutput:
        return FiniteStateMachine.s_reject, input_chars_read


class Colon(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(Colon.s_0)

    def token(self, value: str) -> Token:
        match value:
            case ":":
                return Token.colon(value)
            case _:
                return super().token(value)

    @staticmethod
    def s_0(input_chars_read: int, input_char: str) -> StateAndOutput:
        if input_char == ":":
            return FiniteStateMachine.s_accept, input_chars_read + 1
        else:
            return FiniteStateMachine.s_reject, 0


class Eof(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(Eof.s_0)

    def token(self, value: str) -> Token:
        match value:
            case "":
                return Token.eof(value)
            case _:
                return super().token(value)

    @staticmethod
    def s_0(input_chars_read: int, input_char: str) -> StateAndOutput:
        if input_char == "":
            return FiniteStateMachine.s_accept, input_chars_read + 1
        else:
            return FiniteStateMachine.s_reject, 0


class WhiteSpace(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(WhiteSpace.s_0)

    def token(self, value: str) -> Token:
        return Token.whitespace(value)

    @staticmethod
    def s_0(input_chars_read: int, input_char: str) -> StateAndOutput:
        if input_char in [" ", "\t", "\r", "\n"]:
            return WhiteSpace.s_0, input_chars_read + 1
        elif input_chars_read > 0:
            return FiniteStateMachine.s_accept, input_chars_read
        else:
            return FiniteStateMachine.s_reject, 0
