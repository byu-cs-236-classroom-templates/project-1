"""Finite State Machine (FSM) abstraction.

The finite state machine (FSM) is abstracted by the `FiniteStateMachine` class.
The function `run_fsm(fsm, input_string)` runs the indicated `fsm` until it
accepts or rejects to return the resulting characters read and token.

Note: An FSM normally reads until there are no more characters left in the input
and then it returns `accept` or `reject`. In our application to lexical analysis
we want the FSM to stop reading as soon as it is able to `accept` or `reject`.
As such, for our application, the end of input is marked as soon when the FSM
arrives to the `accept` state or the `reject` state rather than the end of input.
"""

from typing import Callable

from project1.token import Token

State = Callable[[str], "State"]
"""
`State` is a function that takes the character to read as a `str` and returns
the next `State`: `State` : `I` -> `State`.
"""


def run_fsm(fsm: "FiniteStateMachine", input_string: str) -> tuple[int, Token]:
    """Run an FSM and return the number of characters read with the token.

    Run the FSM until it accepts or rejects while counting the number of
    characters read. The return value is a tuple of the number of characters
    and the resulting token if the FSM accepts.

    Args:

        fsm: the FSM to run
        input_string: the string to use as input

    Returns:

        (output_num_chars_read, token): the number of characters read from the input and the associated token produced by the FSM as a tuple

    Examples:

        >>> from project1.fsm import run_fsm, Colon
        >>> colon = Colon()
        >>> input_string = ": a"
        >>> number_chars_read, token = run_fsm(colon, input_string)
        >>> "number_chars_read = {} token = {}".format(number_chars_read, str(token))
        'number_chars_read = 1 token = (COLON,":",0)'
    """
    current_state: State = fsm.initial_state
    next_state: State
    num_chars_read: int = 0
    input_char: str = ""
    len_of_input_string = len(input_string)

    for i in range(0, len_of_input_string + 1):
        input_char = input_string[i] if i < len_of_input_string else ""

        next_state = current_state(input_char)
        match next_state:
            case FiniteStateMachine.s_accept:
                break
            case FiniteStateMachine.s_reject:
                num_chars_read = 0
                break
            case _:
                num_chars_read += 1

        current_state = next_state

    value = input_string[:num_chars_read]
    return (num_chars_read, fsm.token(value))


class FiniteStateMachine:
    """Base class for the finite state machine (FSM) abstraction.

    The base class defines the accept and reject states. The reject state
    will always return zero characters read. Once accept/reject, then always
    accept/reject. The output does not change once in these states. The
    `token` function should be overridden in each subclass.

    Attributes:
        initial_state (State): The initial state for this FSM.
    """

    __slots__ = ["initial_state"]

    def __init__(self, initial_state: State) -> None:
        """Initialize the FSM with its initial state

        Args:
            initial_state: The initial state for this FSM.
        """
        self.initial_state = initial_state

    def token(self, value: str) -> Token:
        """Return the token produced by this FSM

        NOTE: this method must be overridden in any subclass as it defaults to UNDEFINED

        Args:
            value: The value associated with this `Token`.

        Returns:
            Token.undefined: The method must be overridden in subclasses.
        """
        return Token.undefined(value)

    @staticmethod
    def s_accept(input_char: str) -> State:
        """Accept sync state -- once accept always accept."""
        return FiniteStateMachine.s_accept

    @staticmethod
    def s_reject(input_char: str) -> State:
        """Reject sync state -- once reject always reject."""
        return FiniteStateMachine.s_reject


class Colon(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(Colon.s_0)

    def token(self, value: str) -> Token:
        """Create a token of type COLON.

        NOTE: the match statement is for mypy as it ensures that mypy is able to statically
        prove that `value` is ":" when calling `Token.colon(value)`. Follow the pattern for
        other keyword FSMs.

        Args:
            value: The characters read by the FSM.

        Returns:
            Token.colon: iff what is read is a ":" otherwise Token.undefined -- both use `value` for the token.
        """
        match value:
            case ":":
                return Token.colon(value)
            case _:
                return super().token(value)

    @staticmethod
    def s_0(input_char: str) -> State:
        if input_char == ":":
            return Colon.s_1
        else:
            return FiniteStateMachine.s_reject

    @staticmethod
    def s_1(input_char: str) -> State:
        return FiniteStateMachine.s_accept


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
    def s_0(input_char: str) -> State:
        if input_char == "":
            return Eof.s_1
        else:
            return FiniteStateMachine.s_reject

    @staticmethod
    def s_1(input_char: str) -> State:
        return FiniteStateMachine.s_accept


class WhiteSpace(FiniteStateMachine):
    def __init__(self) -> None:
        super().__init__(WhiteSpace.s_0)

    def token(self, value: str) -> Token:
        return Token.whitespace(value)

    @staticmethod
    def s_0(input_char: str) -> State:
        if input_char in [" ", "\t", "\r", "\n"]:
            return WhiteSpace.s_1
        else:
            return FiniteStateMachine.s_reject

    @staticmethod
    def s_1(input_char: str) -> State:
        if input_char in [" ", "\t", "\r", "\n"]:
            return WhiteSpace.s_1
        else:
            return FiniteStateMachine.s_accept
