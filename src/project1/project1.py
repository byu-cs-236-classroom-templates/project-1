from sys import argv

from project1.lexer import lexer


def project1(input_string: str) -> str:
    tokens: str = ""

    for i in lexer(input_string):
        tokens += "\n" + str(i)

    return tokens


def project1cli() -> None:
    if len(argv) == 2:
        input_file = argv[1]
        with open(input_file, "r") as f:
            input_string = f.read()
            result = project1(input_string)
            print(result)
    else:
        print("usage: project1 <input file>")
