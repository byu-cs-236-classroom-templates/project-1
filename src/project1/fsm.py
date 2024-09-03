"""Finite State Machine (FSM) abstraction

Classes:

    FiniteStateMachine: base class for all derivative machines
    Colon: an FSM to create COLON tokens from input
    Eof: an FSM to create EOF tokens from input
    Whitespace: an FSM To create WHITESPACE tokens from input

Functions:

    run_fsm(fsm: "FiniteStateMachine", input_string: str): run an FSM to completion and return the output

Misc:

    State: mypy type definition for `State`
    StateAndOutput: mypy type definition for what is returned from a `State` given input
"""

from typing import Callable
from project1.token import Token


State = Callable[[int, str], "StateAndOutput"]
StateAndOutput = tuple[State, int]


def run_fsm(fsm: "FiniteStateMachine", input_string: str) -> tuple[int, Token]:
    """Runs an FSM and return the number of characters read with the token

    Parameters:

        fsm (FiniteStateMachine): the FSM to run
        input_string (str): the string to use as input

    Returns:

        (output_num_chars_read, token): the number of characters read from the input and the associated token produced by the FSM as a tuple

    Example Usage:

        >>> from project1.fsm import run_fsm, Colon
        >>> colon = Colon()
        >>> input_string = ": a"
        >>> number_chars_read, token = run_fsm(colon, input_string)
        >>> "number_chars_read = {} token = {}".format(number_chars_read, str(token))
        'number_chars_read = 1 token = (COLON,":",0)'
    """
    current_state: State = fsm.initial_state
    next_state: State

    output_num_chars_read: int = 0

    input_num_chars_read: int = 0
    input_char: str = ""

    number_of_chars = len(input_string)
    for i in range(0, number_of_chars + 1):
        input_num_chars_read = output_num_chars_read
        input_char = input_string[i] if i < number_of_chars else ""

        next_state, output_num_chars_read = current_state(
            input_num_chars_read, input_char
        )
        if next_state in {
            FiniteStateMachine.s_accept,
            FiniteStateMachine.s_reject,
        }:
            break

        current_state = next_state

    value = input_string[:output_num_chars_read]
    return (output_num_chars_read, fsm.token(value))


class FiniteStateMachine:
    """Base class for the finite state machine (FSM) abstraction

    Attributes:

        initial_state: State
            the initial state for this FSM

    Methods:

        token(self, value: str):
            create the token produced by the FSM with the indicated value

    Static Methods:

        s_accept(input_chars_read: int, input_char: str):
            the sync state for accept -- once accept always accept
        s_reject(input_chars_read: int, input_char: str):
            the sync state for reject -- once reject always reject
    """

    __slots__ = ["initial_state"]

    def __init__(self, initial_state: State) -> None:
        """Initialize the FSM with the initial state to start in"""
        self.initial_state = initial_state

    def token(self, value: str) -> Token:
        """Return the token produced by this FSM

        NOTE: this method must be overridden as it defaults to UNDEFINED
        """
        return Token.undefined(value)

    @staticmethod
    def s_accept(input_chars_read: int, input_char: str) -> StateAndOutput:
        """Accept sync state -- once accept always accept"""
        return FiniteStateMachine.s_accept, input_chars_read

    @staticmethod
    def s_reject(input_chars_read: int, input_char: str) -> StateAndOutput:
        """Reject sync state -- once reject always reject"""
        return FiniteStateMachine.s_reject, input_chars_read


class Colon(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(Colon.s_0)

    def token(self, value: str) -> Token:
        """Create a token of type COLON

        Parameters:

            value (str): the characters read by the FSM

        Returns:

            Token.colon(value) iff what is read is a ":" otherwise Token.undefined(value)

        NOTE: the match statement is for mypy as it ensures that mypy is able to statically
        prove that `value` is ":" when calling `Token.colon(value)`. Follow the pattern for
        other keyword FSMs.
        """
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
