"""Function to call lexer and got tokens

Functions:

    project1(input_string: str):
        Builds token stream for the input and returns the stream as a string
     project1cli():
        Entry point for the package that expects a file with the input as a command line argument
"""

from sys import argv

from project1.lexer import lexer


def project1(input_string: str) -> str:
    """Build the token stream for a given input

    Parameters:
        input_string (str): the string to tokenize

    Returns:
        the token stream, as a string, from the input string

    Example Usage:

        >>> from project1.project1 import project1
        >>> token_stream = project1('\\n\\n::')
        >>> print(token_stream)
        (COLON,":",3)
        (COLON,":",3)
        (EOF,"",3)
        Total Tokens = 3
    """
    result: str = ""
    token_count = 0
    for i in lexer(input_string):
        result += str(i) + "\n"
        token_count += 1
        if i.token_type == "UNDEFINED":
            return result + "\nTotal Tokens = Error on line " + str(i.line_num)

    return result + "Total Tokens = " + str(token_count)


def project1cli() -> None:
    """Build the token stream from the contents of a file

    From the integrated terminal:

    $ project1 t.txt
    (COLON,":",2)
    (COLON,":",2)
    (COLON,":",2)
    (EOF,"",5)
    Total Tokens = 4
    """
    if len(argv) == 2:
        input_file = argv[1]
        with open(input_file, "r") as f:
            input_string = f.read()
            result = project1(input_string)
            print(result)
    else:
        print("usage: project1 <input file>")
