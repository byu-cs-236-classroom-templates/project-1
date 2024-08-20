from fsm import FiniteStateMachine, StateTransitionFunction, TokenFactory
from token import Token


class MatchWho(FiniteStateMachine):
    def __init__(
        self, initial_state: StateTransitionFunction, token_factory: TokenFactory
    ) -> None:
        super().__init__(initial_state, token_factory)

    def token(self, value: str) -> Token:
        return self._token_factory(value)

    @staticmethod
    def s0(char: str) -> StateTransitionFunction:
        if char == "w":
            return MatchWho.s1
        else:
            return FiniteStateMachine.reject

    @staticmethod
    def s1(char: str) -> StateTransitionFunction:
        if char == "h":
            return MatchWho.s2
        else:
            return FiniteStateMachine.reject

    @staticmethod
    def s2(char: str) -> StateTransitionFunction:
        if char == "o":
            return FiniteStateMachine.accept
        else:
            return FiniteStateMachine.reject


def test_given_MatchWho_when_run_with_who_then_accept():
    # given
    fsm = MatchWho(MatchWho.s0, Token.string)

    # when
    characters_read, token = fsm.run("who", 42)

    # then
    assert 3 == characters_read
    assert str(Token.string("who", 42)) == str(token)
