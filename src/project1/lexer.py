from typing import Iterator

from project1.token import Token, TokenType
from project1.fsm import run_fsm, FiniteStateMachine, Colon, Eof, WhiteSpace


def _get_new_lines(value: str) -> int:
    return len([i for i in value if i == "\n"])


def _get_token(input_str: str, fsms: list[FiniteStateMachine]) -> Token:
    token: Token = Token.undefined(input_str)
    max_chars_read: int = 0
    for i in fsms:
        chars_read, token_i = run_fsm(i, input_str)
        if chars_read > max_chars_read:
            max_chars_read, token = chars_read, token_i
    return token


def _lexer(
    input_string: str, fsms: list[FiniteStateMachine], hidden: list[TokenType]
) -> Iterator[Token]:
    line_num: int = 1
    token: Token = Token.undefined("")
    while token.token_type != "EOF":
        token = _get_token(input_string, fsms)
        token.line_num = line_num
        line_num = line_num + _get_new_lines(token.value)
        input_string = input_string.removeprefix(token.value)
        if token.token_type in hidden:
            continue
        yield token


def lexer(input_string: str) -> Iterator[Token]:
    fsms: list[FiniteStateMachine] = [Colon(), Eof(), WhiteSpace()]
    hidden: list[TokenType] = ["WHITESPACE"]

    for i in _lexer(input_string, fsms, hidden):
        yield i
