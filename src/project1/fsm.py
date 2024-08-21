from typing import Callable
from project1.token import Token


class AcceptException(Exception):
    pass


class RejectException(Exception):
    pass


StateTableRow = Callable[[int, str], "StateTableRowAndOutput"]
StateTableRowAndOutput = tuple[StateTableRow, int]


class FiniteStateMachine:
    __slots__ = ["_initial_row"]

    def __init__(self, initial_row: StateTableRow) -> None:
        self._initial_row = initial_row

    def run(self, input_string: str) -> tuple[int, Token]:
        current_row: StateTableRow = self._initial_row
        next_row: StateTableRow

        output_chars_read: int = 0

        input_chars_read: int = 0
        input_char: str = ""

        number_of_chars = len(input_string)
        for i in range(0, number_of_chars + 1):
            input_chars_read = output_chars_read
            input_char = input_string[i] if i < number_of_chars else ""

            next_row, output_chars_read = current_row(input_chars_read, input_char)
            if next_row in {
                FiniteStateMachine.row_accept,
                FiniteStateMachine.row_reject,
            }:
                break

            current_row = next_row

        value = input_string[:output_chars_read]
        return (output_chars_read, self.token(value))

    def token(self, value: str) -> Token:
        return Token.undefined(value)

    @staticmethod
    def row_accept(input_chars_read: int, input_char: str) -> StateTableRowAndOutput:
        return FiniteStateMachine.row_accept, input_chars_read

    @staticmethod
    def row_reject(input_chars_read: int, input_char: str) -> StateTableRowAndOutput:
        return FiniteStateMachine.row_reject, input_chars_read


class Colon(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(Colon.row_0)

    def token(self, value: str) -> Token:
        match value:
            case ":":
                return Token.colon(value)
            case _:
                return super().token(value)

    @staticmethod
    def row_0(input_chars_read: int, input_char: str) -> StateTableRowAndOutput:
        if input_char == ":":
            return FiniteStateMachine.row_accept, input_chars_read + 1
        else:
            return FiniteStateMachine.row_reject, 0


class Eof(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(Eof.row_0)

    def token(self, value: str) -> Token:
        match value:
            case "":
                return Token.eof(value)
            case _:
                return super().token(value)

    @staticmethod
    def row_0(input_chars_read: int, input_char: str) -> StateTableRowAndOutput:
        if input_char == "":
            return FiniteStateMachine.row_accept, input_chars_read + 1
        else:
            return FiniteStateMachine.row_reject, 0


class WhiteSpace(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(WhiteSpace.row_0)

    def token(self, value: str) -> Token:
        return Token.whitespace(value)

    @staticmethod
    def row_0(input_chars_read: int, input_char: str) -> StateTableRowAndOutput:
        if input_char in [" ", "\t", "\r", "\n"]:
            return WhiteSpace.row_0, input_chars_read + 1
        elif input_chars_read > 0:
            return FiniteStateMachine.row_accept, input_chars_read
        else:
            return FiniteStateMachine.row_reject, 0
