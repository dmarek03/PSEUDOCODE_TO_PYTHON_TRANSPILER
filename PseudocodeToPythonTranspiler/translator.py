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

    @staticmethod
    def cast_to_python_type(data_type: str) -> str:
        type_mapping = {
            "INTEGER": "int",
            "REAL": "float",
            "CHAR": "str",
            "STRING": "str",
            "BOOLEAN": "bool",
        }
        return type_mapping.get(data_type.upper(), "Any")

    def indent(self):

        return "    " * self.indent_level

    def visitProgram(self, ctx):

        result = []

        for statement in ctx.statement_list().statement():
            result.append(self.visit(statement))

        return "\n".join(result)

    def visitDeclaration(self, ctx):

        var_name = ctx.IDENTIFIER().getText()
        data_type = ctx.data_type().getText()

        if not self.declared_variables.get(var_name):
            self.declared_variables[var_name] = data_type

            if data_type in ["INTEGER", "REAL", "STRING", "BOOLEAN"]:
                return ""
            if data_type.startswith("ARRAY"):

                return self.handleArrayDeclaration(var_name, data_type)

        else:

            return ""

    def handleArrayDeclaration(self, var_name, data_type):

        array_type_parts = data_type.split("OF", 1)
        elements_number_part = array_type_parts[0]
        array_type = array_type_parts[-1].strip()

        elements_number = (
            elements_number_part.replace("ARRAY[", "").replace("]", "").strip()
        )

        if array_type.startswith("ARRAY"):

            inner_array_declaration = self.handleArrayDeclaration(
                var_name, array_type
            ).replace(f"{var_name} = ", "")

            return f"{var_name} = [{inner_array_declaration} for _ in range({elements_number})]"

        match array_type:
            case "INTEGER":
                x = 0
            case "REAL":
                x = 0.0
            case "BOOLEAN":
                x = False
            case _:
                x = 0

        return f"{var_name} = [{x} for _ in range({elements_number})]"

    def visitAssignment(self, ctx):

        var_name = ctx.IDENTIFIER().getText()

        if ctx.LBRACKET():

            index = self.visit(ctx.expression(0))

            value = self.visit(ctx.expression(1))

            return f"{var_name}[{index}] = {value}"

        value = self.visit(ctx.expression(0))

        if self.declared_variables.get(var_name):

            return f"{var_name} = {value}"
        else:

            self.declared_variables[var_name] = value
            return f"{var_name} = {value}"

    def visitCast(self, ctx):

        value = self.visit(ctx.expression())

        target_type = ctx.type_().getText()

        if target_type == "REAL":
            return f"float({value})"
        elif target_type == "INTEGER":
            return f"int({value})"
        elif target_type == "STRING":
            return f"str({value})"
        else:

            return f"#Unsupported cast: {ctx.getText()}"


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