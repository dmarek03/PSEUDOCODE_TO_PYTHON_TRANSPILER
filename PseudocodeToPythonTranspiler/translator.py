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

    def visitExpression(self, ctx):
        return self.visit(ctx.additionExpression())

    def visitReturn_statement(self, ctx):

        return_value = self.visit(ctx.expression())
        return f"return {return_value}"

    def visitComment_statement(self, ctx):

        if ctx.ONE_LINE_COMMENT():
            comment_text = ctx.ONE_LINE_COMMENT().getText().lstrip("//")
            return f"# {comment_text.strip()}"

        if ctx.MULTIPLE_LINE_COMMENT():

            comment_text = (
                ctx.MULTIPLE_LINE_COMMENT().getText().strip("***").strip("***")
            )

            lines = comment_text.splitlines()

            return f'"""' + "\n".join([line.strip() for line in lines]) + "\n" + '"""'

        return f"# Unknown comment type"

    def visitAdditionExpression(self, ctx):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicationExpression())

        left = self.visit(ctx.additionExpression())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.multiplicationExpression())

        return f"({left} {op} {right})"

    def visitMultiplicationExpression(self, ctx):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.primaryExpression())

        left = self.visit(ctx.multiplicationExpression())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.primaryExpression())

        return f"({left} {op} {right})"

    def visitPrimaryExpression(self, ctx):

        if hasattr(ctx, "cast") and ctx.cast():

            return self.visit(ctx.cast())

        if ctx.term():
            return self.visit(ctx.term())

        if ctx.file_handling():
            return "".join(self.visit(ctx.file_handling()).split(" ")[2:])

        elif ctx.IDENTIFIER() and ctx.LBRACKET() and ctx.RBRACKET():  # Array access
            identifier = ctx.IDENTIFIER().getText()
            index = self.visit(ctx.expression(0))
            return f"{identifier}[{index}]"

        if ctx.getChildCount() == 6:
            func = ctx.getChild(0).getText()
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            if func == "DIV":
                return f"({left} // {right})"
            elif func == "MOD":
                return f"({left} % {right})"

        if ctx.LPAREN() and ctx.RPAREN():

            if isinstance(ctx.expression(), list) and len(ctx.expression()) > 0:
                nested = self.visit(ctx.expression(0))
            else:
                nested = self.visit(ctx.expression())
            return f"({nested})"

        return f"# Unsupported primary expression: {ctx.getText()} "

    def visitTerm(self, ctx):

        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.literal():

            return self.visit(ctx.literal())
        elif ctx.function_call():
            return self.visit(ctx.function_call())

        return f"# Unsupported term: {ctx.getText()}"

    def visitLiteral(self, ctx):

        if ctx.NUMBER():
            return ctx.NUMBER().getText()

        elif ctx.REAL_NUMBER():
            return ctx.REAL_NUMBER().getText()
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()
        elif ctx.CHAR_LITERAL():
            return ctx.CHAR_LITERAL().getText()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"

        return f"# Unsupported literal: {ctx.getText()}"

    def visitIf_statement(self, ctx):

        condition = self.visit(ctx.condition())

        self.indent_level += 1
        then_block = "\n".join(
            [
                self.indent() + self.visit(stmt)
                for stmt in ctx.statement_list(0).statement()
            ]
        )
        self.indent_level -= 1

        if ctx.ELSE():
            self.indent_level += 1
            else_block = "\n".join(
                [
                    self.indent() + self.visit(stmt)
                    for stmt in ctx.statement_list(1).statement()
                ]
            )
            self.indent_level -= 1
            return f"if {condition}:\n{then_block}\n{self.indent()}else:\n{else_block}"
        else:
            return f"if {condition}:\n{then_block}"

    def visitCondition(self, ctx):

        if ctx.LPAREN():
            inner_condition = self.visit(ctx.condition(0))
            return f"({inner_condition})"

        if ctx.NOT():
            inner_condition = self.visit(ctx.condition(0))
            return f"not {inner_condition}"

        if ctx.AND():
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            return f"({left} and {right})"

        if ctx.OR():
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            return f"({left} or {right})"

        if ctx.comparison_operator():
            left = self.visit(ctx.expression(0))
            op = ctx.comparison_operator().getText()
            python_op = {"=": "==", "<>": "!="}.get(op, op)
            right = self.visit(ctx.expression(1))
            return f"{left} {python_op} {right}"

        condition_text = ctx.getText()

        return f"# Unsupported condition: {condition_text}"

    def visitCase_statement(self, ctx):
        variable = ctx.IDENTIFIER().getText()
        case_blocks = []

        self.indent_level += 1
        for case_ctx in ctx.case_list().case():
            if case_ctx.literal():
                case_value = self.visit(case_ctx.literal())

                self.indent_level += 1
                statements = "\n".join(
                    [
                        self.indent() + self.visit(stmt)
                        for stmt in case_ctx.statement_list().statement()
                    ]
                )
                self.indent_level -= 1
                case_blocks.append(f"{self.indent()}case {case_value}:\n{statements}")
            elif case_ctx.OTHERWISE():
                self.indent_level += 1
                statements = "\n".join(
                    [
                        self.indent() + self.visit(stmt)
                        for stmt in case_ctx.statement_list().statement()
                    ]
                )
                self.indent_level -= 1
                case_blocks.append(f"{self.indent()}case _:\n{statements}")

        self.indent_level -= 1

        match_code = f"{self.indent()}match {variable}:\n" + "\n".join(case_blocks)
        return match_code

    def visitOutput(self, ctx):

        values = ctx.value_list().expression()

        formatted_values = []

        for value in values:

            if value.getText().startswith('"') and value.getText().endswith('"'):

                formatted_values.append(value.getText().strip('"'))
            else:

                formatted_values.append(f"{{{self.visit(value)}}}")

        if len(values) == 1:

            python_code = f"print({values[0].getText()})"
        else:

            python_code = f'print(f"{"".join(formatted_values)}")'

        return python_code

    def visitInput(self, ctx):

        var_name = ctx.IDENTIFIER().getText()

        cast_map = {"INTEGER": "int", "REAL": "float", "BOOLEAN": "bool"}
        cast = cast_map.get(self.declared_variables.get(var_name, ""), None)
        if cast:
            return f"{var_name} = {cast}(input('Enter data: '))"
        else:
            return f"{var_name} = input('Enter data: ')"

    def visitWhile_loop(self, ctx):

        condition = self.visit(ctx.condition())
        self.indent_level += 1
        body = "\n".join(
            [
                self.indent() + self.visit(stmt)
                for stmt in ctx.statement_list().statement()
            ]
        )
        self.indent_level -= 1
        return f"while {condition}:\n{body}"

    def visitFor_loop(self, ctx):

        try:

            var_name = ctx.IDENTIFIER(0).getText()
            start = self.visit(ctx.expression(0))
            end = self.visit(ctx.expression(1))
            step = self.visit(ctx.expression(2)) if ctx.STEP() else None

            range_exp = f"{start}, {end}" + (f", {step}" if step else "")

            self.indent_level += 1

            body = "\n".join(
                [
                    self.indent() + self.visit(stmt)
                    for stmt in ctx.statement_list().statement()
                ]
            )
            self.indent_level -= 1

            return f"for {var_name} in range({range_exp}):\n{body}"
        except Exception as e:

            return f"# Error in visitFor_loop: {e} "

    def visitRepeat_until_loop(self, ctx):

        self.indent_level += 1
        body = "\n".join(
            [
                self.indent() + self.visit(stmt)
                for stmt in ctx.statement_list().statement()
            ]
        )
        self.indent_level -= 1
        condition = self.visit(ctx.condition())
        return f"while True:\n{body}\n{self.indent()}if {condition}:\n{self.indent()}    break"




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