from .fsa_classes.fsa import FSA
from .fsa_classes.colon_dash_fsa import ColonDashFSA
from .token import Token

class LexerFSM:
    def __init__(self):
        self.tokens: list[Token] = []
        self.colon_dash_fsa: ColonDashFSA = ColonDashFSA()
        # other FSA classes and any other member variables you need
    
    def run(self, input: str) -> str:
        ...   
    
    def lex(self, input_string: str) -> Token:
        ...

    def __manager_fsm__(self) -> Token:
        ...

    def reset(self) -> None:
        ...