from project1.fsm import Colon, WhiteSpace, Eof
from project1.token import Token


class TestColon:
    def test_given_non_colon_when_run_then_reject(self):
        # given
        colon = Colon()
        input_string = "abc  \n \t"

        # when
        number_chars_read, _ = colon.run(input_string)

        # then
        assert 0 == number_chars_read

    def test_given_colon_when_run_then_accept(self):
        # given
        whitespace = Colon()
        input_string = ": \r\n\r\n \n \t \t  ab c d"

        # when
        number_chars_read, token = whitespace.run(input_string)

        # then
        assert 1 == number_chars_read
        assert str(Token.colon(":")) == str(token)


class TestEof:
    def test_given_non_eof_when_run_then_reject(self):
        # given
        eof = Eof()
        input_string = "abc  \n \t"

        # when
        number_chars_read, _ = eof.run(input_string)

        # then
        assert 0 == number_chars_read

    def test_given_eof_when_run_then_accept(self):
        # given
        eof = Eof()
        input_string = ""

        # when
        number_chars_read, token = eof.run(input_string)

        # then
        assert 1 == number_chars_read
        assert str(Token.eof("")) == str(token)


class TestWhiteSpace:
    def test_given_non_white_space_when_run_then_reject(self):
        # given
        whitespace = WhiteSpace()
        input_string = "abc  \n \t"

        # when
        number_chars_read, _ = whitespace.run(input_string)

        # then
        assert 0 == number_chars_read

    def test_given_white_space_when_run_then_accept(self):
        # given
        whitespace = WhiteSpace()
        input_string = " \r\n\r\n \n \t \t  ab c d"

        # when
        number_chars_read, token = whitespace.run(input_string)

        # then
        assert 13 == number_chars_read
        assert str(Token.whitespace(" \r\n\r\n \n \t \t  ")) == str(token)
