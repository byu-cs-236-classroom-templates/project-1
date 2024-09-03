from typing import Literal, Any

# `TokenType` is an algebraic data type, and more specifically, it is a "sum type". A sum type gives a list of allowed types, or in this case, allowed string literals that belong to `TokenType`.
# The mypy tool uses `TokenType` to statically check that the string values used to create tokens are type safe. For example, when using `Token.colon(value)` to create a colon token, mypy must be able to prove that `value` is equivalent to ":".
# `TokenType` is complete meaning that it has all the allowed tokens for project 1.
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
    __slots__ = ["token_type", "value", "line_num"]

    def __init__(self, token_type: TokenType, value: str, line_num: int = 0) -> None:
        """Initialize a `Token` with its type, value, and line number

        Use the static factory methods to create instances of `Token` as they restrict tokens to those allowed by `TokenType`
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

    @staticmethod
    def colon(value: Literal[":"]) -> "Token":
        return Token("COLON", value)

    @staticmethod
    def colon_dash(value: Literal[":-"]) -> "Token":
        return Token("COLON_DASH", value)

    @staticmethod
    def comma(value: Literal[","]) -> "Token":
        return Token("COMMA", value)

    @staticmethod
    def comment(value: str) -> "Token":
        return Token("COMMENT", value)

    @staticmethod
    def undefined(value: str) -> "Token":
        return Token("UNDEFINED", value)

    @staticmethod
    def eof(value: Literal[""]) -> "Token":
        return Token("EOF", value)

    @staticmethod
    def facts(value: Literal["Facts"]) -> "Token":
        return Token("FACTS", value)

    @staticmethod
    def id(value: str) -> "Token":
        return Token("ID", value)

    @staticmethod
    def left_paren(value: Literal["("]) -> "Token":
        return Token("LEFT_PAREN", value)

    @staticmethod
    def period(value: Literal["."]) -> "Token":
        return Token("PERIOD", value)

    @staticmethod
    def queries(value: Literal["Queries"]) -> "Token":
        return Token("QUERIES", value)

    @staticmethod
    def q_mark(value: Literal["?"]) -> "Token":
        return Token("Q_MARK", value)

    @staticmethod
    def right_paren(value: Literal[")"]) -> "Token":
        return Token("RIGHT_PAREN", value)

    @staticmethod
    def rules(value: Literal["Rules"]) -> "Token":
        return Token("RULES", value)

    @staticmethod
    def schemes(value: Literal["Schemes"]) -> "Token":
        return Token("SCHEMES", value)

    @staticmethod
    def string(value: str) -> "Token":
        return Token("STRING", value)

    @staticmethod
    def whitespace(value: str) -> "Token":
        for i in value:
            assert i == " " or i == "\t" or i == "\n" or i == "\r"
        return Token("WHITESPACE", value)
