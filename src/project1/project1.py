from sys import argv

from project1.lexer import lexer


def project1(input_string: str) -> str:
    result: str = ""
    token_count = 0
    for i in lexer(input_string):
        result += str(i) + "\n"
        token_count += 1
        if i.token_type == "UNDEFINED":
            return result + "\nTotal Tokens = Error on line " + str(i.line_num)

    return result + "Total Tokens = " + str(token_count)


def project1cli() -> None:
    if len(argv) == 2:
        input_file = argv[1]
        with open(input_file, "r") as f:
            input_string = f.read()
            result = project1(input_string)
            print(result)
    else:
        print("usage: project1 <input file>")
