import black
from antlr4 import *
from grammar_utils.PseudoCodeLexer import PseudoCodeLexer
from grammar_utils.PseudoCodeParser import PseudoCodeParser
from grammar_utils.PseudoCodeVisitor import PseudoCodeVisitor


class PseudoCodeToPythonVisitor(PseudoCodeVisitor):
    def __init__(self):
        super().__init__()
        self.indent_level = 0
        self.declared_variables = {}


def translate_pseudocode_to_python(input_file, output_file):

    input_stream = FileStream("input_files/" + input_file, encoding="utf-8")
    lexer = PseudoCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PseudoCodeParser(token_stream)
    tree = parser.program()

    visitor = PseudoCodeToPythonVisitor()
    python_code = visitor.visit(tree)

    with open("output_files/" + output_file, "w") as f:
        f.write(python_code)

    try:
        black.format_file_in_place(
            src=black.Path("output_files/" + output_file),
            fast=False,
            mode=black.FileMode(),
            write_back=black.WriteBack.YES,
        )
        print(f"Plik {output_file} został sformatowany za pomocą Black.")
    except Exception as e:
        print(f"Nie udało się sformatować pliku {output_file}: {e}")


def main() -> None:
    translate_pseudocode_to_python(input_file="test.pseudo", output_file="test.py")


if __name__ == "__main__":
    main()