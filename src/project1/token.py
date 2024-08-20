from typing import Literal

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

    def __init__(self, token_type: TokenType, value: str, line_num: int):
        self.token_type: TokenType = token_type
        self.value: str = value
        self.line_num: int = line_num

    def __str__(self) -> str:
        return (
            "(" + self.token_type + ',"' + self.value + '",' + str(self.line_num) + ")"
        )

    @staticmethod
    def colon(value: Literal[":"], line_num: int) -> "Token":
        assert ":" == value
        return Token("COLON", value, line_num)

    @staticmethod
    def colon_dash(value: Literal[":-"], line_num: int) -> "Token":
        assert ":-" == value
        return Token("COLON_DASH", value, line_num)

    @staticmethod
    def comma(value: Literal[","], line_num: int) -> "Token":
        assert "," == value
        return Token("COMMA", value, line_num)

    @staticmethod
    def comment(value: str, line_num: int) -> "Token":
        return Token("COMMENT", value, line_num)

    @staticmethod
    def undefined(value: str, line_num: int) -> "Token":
        return Token("UNDEFINED", value, line_num)

    @staticmethod
    def eof(value: Literal[""], line_num: int) -> "Token":
        assert "" == value
        return Token("EOF", value, line_num)

    @staticmethod
    def facts(value: Literal["Facts"], line_num: int) -> "Token":
        assert "Facts" == value
        return Token("FACTS", value, line_num)

    @staticmethod
    def id(value: str, line_num: int) -> "Token":
        return Token("ID", value, line_num)

    @staticmethod
    def left_paren(value: Literal["("], line_num: int) -> "Token":
        assert "(" == value
        return Token("LEFT_PAREN", value, line_num)

    @staticmethod
    def period(value: Literal["."], line_num: int) -> "Token":
        assert "." == value
        return Token("PERIOD", value, line_num)

    @staticmethod
    def queries(value: Literal["Queries"], line_num: int) -> "Token":
        assert "Queries" == value
        return Token("QUERIES", value, line_num)

    @staticmethod
    def q_mark(value: Literal["?"], line_num: int) -> "Token":
        assert "?" == value
        return Token("Q_MARK", value, line_num)

    @staticmethod
    def right_paren(value: Literal[")"], line_num: int) -> "Token":
        assert ")" == value
        return Token("RIGHT_PAREN", ")", line_num)

    @staticmethod
    def rules(value: Literal["Rules"], line_num: int) -> "Token":
        assert "Rules" == value
        return Token("RULES", "Rules", line_num)

    @staticmethod
    def schemes(value: Literal["Schemes"], line_num: int) -> "Token":
        assert "Schemes" == value
        return Token("SCHEMES", "Schemes", line_num)

    @staticmethod
    def string(value: str, line_num: int) -> "Token":
        return Token("STRING", value, line_num)

    @staticmethod
    def whitespace(value: str, line_num: int) -> "Token":
        for i in value:
            assert i == " " or i == "\t" or i == "\n" or i == "\r"
        return Token("WHITESPACE", value, line_num)
