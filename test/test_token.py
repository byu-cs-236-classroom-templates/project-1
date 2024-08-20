import pytest
from project1.token import Token


def test_given_mismatched_value_when_Token_then_raise_exception():
    # given
    # "?" for ":"

    # then
    with pytest.raises(Exception):
        # when
        Token.colon("?", 42)


str_test_inputs = [
    (Token.colon(":", 42), '(COLON,":",42)'),
    (Token.colon_dash(":-", 42), '(COLON_DASH,":-",42)'),
    (Token.comma(",", 42), '(COMMA,",",42)'),
    (Token.comment("# line comment", 42), '(COMMENT,"# line comment",42)'),
    (
        Token.undefined("lots of undefined stuff", 42),
        '(UNDEFINED,"lots of undefined stuff",42)',
    ),
    (Token.eof("", 42), '(EOF,"",42)'),
    (Token.facts("Facts", 42), '(FACTS,"Facts",42)'),
    (Token.id("id", 42), '(ID,"id",42)'),
    (Token.left_paren("(", 42), '(LEFT_PAREN,"(",42)'),
    (Token.period(".", 42), '(PERIOD,".",42)'),
    (Token.queries("Queries", 42), '(QUERIES,"Queries",42)'),
    (Token.q_mark("?", 42), '(Q_MARK,"?",42)'),
    (Token.right_paren(")", 42), '(RIGHT_PAREN,")",42)'),
    (Token.rules("Rules", 42), '(RULES,"Rules",42)'),
    (Token.schemes("Schemes", 42), '(SCHEMES,"Schemes",42)'),
    (Token.string("string", 42), '(STRING,"string",42)'),
    (Token.whitespace(" \t\r\n", 42), '(WHITESPACE," \t\r\n",42)'),
]
str_test_ids = [
    "colon",
    "colon_dash",
    "comma",
    "comment",
    "undefined",
    "eof",
    "facts",
    "id",
    "left_paren",
    "period",
    "queries",
    "q_mark",
    "right_paren",
    "rules",
    "schemes",
    "string",
    "whitespace",
]


@pytest.mark.parametrize("token, expected", str_test_inputs, ids=str_test_ids)
def test_given_good_token_when_str_then_match_expected(token: Token, expected: str):
    # given
    # token

    # when
    result = str(token)

    # then
    assert expected == result
