from project1_classes.lexer_fsm import LexerFSM

# Return your program output here for grading (can treat this function as your "main")
def project1(input: str) -> str:
    lexer: LexerFSM = LexerFSM()
    lexer.run(input)
    return "This is my answer!"

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read() 

# Use this to run and debug code within VS Code
if __name__ == "__main__":
    input_contents = read_file_contents("./project1-passoff/20/input21.txt") # Put path to input file here
    print(project1(input_contents))
