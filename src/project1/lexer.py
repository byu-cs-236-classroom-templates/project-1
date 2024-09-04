"""Turn a input string into a stream of tokens with lexical analysis.

The `lexer(input_string: str)` function is the entry point. It generates a
stream of tokens from the `input_string`.

Typical usage example:

    >>> from project1.lexer import lexer
    >>> input_string = ":\\n  \\n:"
    >>> for i in lexer(input_string):
    ...     print(i)
    ...
    (COLON,":",1)
    (COLON,":",3)
    (EOF,"",3)
"""

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
    """Produce a stream of tokens from a given input string.

    Pseudo-code:

    ```
    fsms: list[FiniteStateMachine] = [Colon(), Eof(), WhiteSpace()]
    hidden: list[TokenType] = ["WHITESPACE"]
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
    ```

    The `_get_token` function should return the token from the FSM that reads
    the most characters. In the case of two FSMs reading the same number of
    characters, the one that comes first in the list of FSMs, `fsms`, wins.

    Args:

        input_string (str): input string for token generation

    Yields:

        token (Token): the current token resulting from the string
    """
    fsms: list[FiniteStateMachine] = [Colon(), Eof(), WhiteSpace()]
    hidden: list[TokenType] = ["WHITESPACE"]

    # raise NotImplementedError
    for i in _lexer(input_string, fsms, hidden):
        yield i
