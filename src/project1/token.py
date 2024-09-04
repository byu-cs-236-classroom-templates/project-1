"""Token class with types and factory methods

Classes:

    Token: the basic type produced by the lexer

Misc:

    TokenType: sum type listing allowed tokens
"""

from typing import Literal, Any


# `TokenType` is an algebraic data type, and more specifically, it is a
# "sum type". A sum type gives a list of allowed types, or in this case,
# allowed string literals that belong to `TokenType`. The mypy tool uses
# `TokenType` to statically check that the string indicating the type of
# token to create belongs to the TokenType sum type.
#
# For more on algebraic types in Python see
# https://threeofwands.com/algebraic-data-types-in-python/

TokenType = Literal[
    "COLON",
    "COLON_DASH",
    "COMMA",
    "COMMENT",
    "UNDEFINED",
    "EOF",
    "FACTS",
    "ID",
    "LEFT_PAREN",
    "PERIOD",
    "QUERIES",
    "Q_MARK",
    "RIGHT_PAREN",
    "RULES",
    "SCHEMES",
    "STRING",
    "WHITESPACE",
]


class Token:
    """A class to represent a token

    Attributes:

        token_type: TokenType
            the type of this token
        value: str
            the string associated with the token
        line_num: int
            the line number associated with the token -- where it starts in the input

    Static Methods -- called as Token.colon(":") for example:

        colon(value: Literal[":"]):
            Returns a token of type "COLON" with value ":"
        colon_dash(value: Literal[":-"]):
            Returns a token of type "COLON_DASH" with value ":-"
        comma(value: Literal[","]):
            Returns a token of type "COMMA" with value ","
        comment(value: str):
            Returns a token of type "COMMENT" with value given by the parameter
        undefined(value: str):
            Returns a token of type "UNDEFINED" with value given by the parameter
        eof(value: Literal[""]):
            Returns a token of type "EOF" with value ""
        facts(value: Literal["Facts"]):
            Returns a token of type "FACTS" with "Facts" as the value
        id(value: str):
            Returns a token of type "ID" with value given by the parameter
        left_paren(value: Literal["("]):
            Returns a token of type "LEFT_PAREN" with "(" as the value
        period(value: Literal["."]):
            Returns a token af type "PERIOD" with "." as the value
        queries(value: Literal["Queries"]):
            Returns a token of type "QUERIES" with "Queries" as the value
        q_mark(value: Literal["?"]):
            Returns a token of type "Q_MARK" with "?" as the value
        right_paren(value: Literal[")"]):
            Returns a token of type "RIGHT_PAREN" with ")" as the value
        rules(value: Literal["Rules"]):
            Returns a token of type "RULES" with "Rules" as the value
        schemes(value: Literal["Schemes"]):
            Returns a token of type "SCHEMES" with "Schemes" as the value
        string(value: str):
            Returns a token of type "STRING" with value given by the parameter
        whitespace(value: str):
            Returns a token af type "WHITESPACE" with value given by the parameter

    Example usage

        >>> from project1.token import Token
        >>> colon = Token.colon(":")
        >>> colon.line_num = 10
        >>> print(colon)
        (COLON,":",10)
        >>> id = Token.id("id")
        >>> id.line_num = 42
        >>> print(id)
        (ID,"id",42)
    """

    __slots__ = ["token_type", "value", "line_num"]

    def __init__(self, token_type: TokenType, value: str, line_num: int = 0) -> None:
        """Initialize a `Token` with its type, value, and line number

        Parameters:
            token_type (TokenType): the type of this token
            value (str): the value to use for this taken
            line_num (int): the line number from the input where the token value begins


        NOTE: use the static factory methods to create instances of `Token`
        """
        self.token_type: TokenType = token_type
        self.value: str = value
        self.line_num: int = line_num

    def __str__(self) -> str:
        return (
            "(" + self.token_type + ',"' + self.value + '",' + str(self.line_num) + ")"
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Token):
            return (
                self.token_type == other.token_type
                and self.value == other.value
                and self.line_num == other.line_num
            )
        return False

    # Any of the methods than name a `Literal` as the type mean that mypy must
    # be able to statically prove the passed in parameter matches the named
    # literal in order for mypy to not report an error.
    # See `fsm.py` for examples to how to help mypy with the proof.

    @staticmethod
    def colon(value: Literal[":"]) -> "Token":
        """Create a COLON token with ':' as its value"""
        return Token("COLON", value)

    @staticmethod
    def colon_dash(value: Literal[":-"]) -> "Token":
        """Create a "COLON_DASH token with ':-' as its value"""
        return Token("COLON_DASH", value)

    @staticmethod
    def comma(value: Literal[","]) -> "Token":
        """Create a COMMA token with ',' as its value"""
        return Token("COMMA", value)

    @staticmethod
    def comment(value: str) -> "Token":
        """Create a COMMENT token with value"""
        return Token("COMMENT", value)

    @staticmethod
    def undefined(value: str) -> "Token":
        """Create an UNDEFINED token with value"""
        return Token("UNDEFINED", value)

    @staticmethod
    def eof(value: Literal[""]) -> "Token":
        """Create an EOF token"""
        return Token("EOF", value)

    @staticmethod
    def facts(value: Literal["Facts"]) -> "Token":
        """Create a FACTS token with 'Facts' as its value"""
        return Token("FACTS", value)

    @staticmethod
    def id(value: str) -> "Token":
        """Create an ID token with value"""
        return Token("ID", value)

    @staticmethod
    def left_paren(value: Literal["("]) -> "Token":
        """Create a LEFT_PAREN token with '(' as its value"""
        return Token("LEFT_PAREN", value)

    @staticmethod
    def period(value: Literal["."]) -> "Token":
        """Create a PERIOD token with '.' as its value"""
        return Token("PERIOD", value)

    @staticmethod
    def queries(value: Literal["Queries"]) -> "Token":
        """Create a QUERIES token with 'Queries' as its value"""
        return Token("QUERIES", value)

    @staticmethod
    def q_mark(value: Literal["?"]) -> "Token":
        """Create a Q_MARK token with '?' as its value"""
        return Token("Q_MARK", value)

    @staticmethod
    def right_paren(value: Literal[")"]) -> "Token":
        """Create a RIGHT_PAREN token with ')' as its value"""
        return Token("RIGHT_PAREN", value)

    @staticmethod
    def rules(value: Literal["Rules"]) -> "Token":
        """Create a RULES token with 'Rules' as its value"""
        return Token("RULES", value)

    @staticmethod
    def schemes(value: Literal["Schemes"]) -> "Token":
        """Create a SCHEMES token with 'Schemes' as its value"""
        return Token("SCHEMES", value)

    @staticmethod
    def string(value: str) -> "Token":
        """Create a STRING token with the value"""
        return Token("STRING", value)

    @staticmethod
    def whitespace(value: str) -> "Token":
        """Create a WHITESPACE token with only whitespace in the value"""
        for i in value:
            assert i == " " or i == "\t" or i == "\n" or i == "\r"
        return Token("WHITESPACE", value)
