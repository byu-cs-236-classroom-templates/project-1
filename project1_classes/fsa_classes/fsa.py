from typing import Callable

class FSA:
    def __init__(self):
        ...
    
    def S0(self) -> Callable:
        raise NotImplementedError()
    
    def run(self, input_string: str) -> bool:
        ...

    def reset(self) -> None:
        ...

    def get_name(self) -> str: 
        ...

    def set_name(self, FSA_name) -> None:
        ...

    def __get_current_input(self) -> str:  # The double underscore makes the method private
        ...