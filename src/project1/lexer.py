from typing import Iterator
from project1.token import Token, TokenType
from project1.fsm import FiniteStateMachine


def _lexer(
    input_string: str, fsms: list[FiniteStateMachine], hidden: list[TokenType]
) -> Iterator[Token]:
    raise NotImplementedError


def lexer(input_string: str) -> Iterator[Token]:
    fsms: list[FiniteStateMachine] = []
    hidden: list[TokenType] = ["WHITESPACE"]

    for i in _lexer(input_string, fsms, hidden):
        yield i
