import pytest

from project1.lexer import lexer

inputs = [
    (": ", ['(COLON,":",1)', '(EOF,"",1)']),
    (" \t\r\n\n: ", ['(COLON,":",3)', '(EOF,"",3)']),
    ("   undefined\n\t", ['(UNDEFINED,"undefined\n\t",1)', '(EOF,"",2)']),
]
ids = [
    "colon",
    "colon-line",
    "undefined",
]


@pytest.mark.parametrize("test_input, expected", inputs, ids=ids)
def test_given_input_when_lexer_then_match_tokens(test_input: str, expected: list[str]):
    # given
    # input
    print(test_input)
    # went
    tokens = [str(i) for i in lexer(test_input)]

    # then
    assert len(expected) == len(tokens)
    assert expected == tokens
