import black
import argparse
import subprocess
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
        is_interpolation_needed = False

        for value in values:
            result = self.visit(value)


            if value.getText().startswith('"') and value.getText().endswith('"'):
                formatted_values.append(value.getText().strip('"'))
            else:
                is_interpolation_needed = True
                formatted_values.append(f"{{{result}}}")

        if len(values) == 1 and not is_interpolation_needed:

            python_code = f'print("{formatted_values[0]}")'
        else:

            joined_values = "".join(formatted_values)
            python_code = f'print(f"{joined_values}")'

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

    def visitFunction_call(self, ctx):

        if ctx.user_function_call():
            func_name = ctx.user_function_call().IDENTIFIER().getText()
            args = ", ".join(
                [
                    self.visit(arg)
                    for arg in ctx.user_function_call().argument_list().expression()
                ]
            )
            return f"{func_name}({args})"

        if ctx.builtin_function_call():

            return self.visit(ctx.builtin_function_call())

    def visitBuiltin_function_call(self, ctx):

        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()

        elif ctx.STRING_LITERAL():
            var_name = ctx.STRING_LITERAL().getText()
        elif ctx.CHAR_LITERAL():
            var_name = ctx.CHAR_LITERAL().getText()
        else:
            var_name = None

        if ctx.LENGTH():

            return f"len({var_name})"
        elif ctx.LCASE():

            return f"{var_name}.lower()"
        elif ctx.UCASE():

            return f"{var_name}.upper()"
        elif ctx.SUBSTRING():

            start = ctx.NUMBER(0)
            end = ctx.NUMBER(1)
            step = ctx.NUMBER(2) if ctx.NUMBER(2) else None
            slicing_expr = "[" + f"{start}:{end}" + (f":{step}" if step else "") + "]"

            return f"{var_name}{slicing_expr}"
        elif ctx.ROUND():
            value = self.visit(ctx.expression(0))
            places = self.visit(ctx.expression(1))
            return f"round({value}, {places})"
        elif ctx.RANDOM():
            return "random.random()"

    def visitProcedure_call(self, ctx):

        proc_name = ctx.IDENTIFIER().getText()
        args = ", ".join([self.visit(arg) for arg in ctx.argument_list().expression()])
        return f"{proc_name}({args})"

    def visitUser_function_definition(self, ctx):

        func_name = ctx.IDENTIFIER().getText()

        params_with_types = []
        for param in ctx.parameter_list().parameter():
            param_name = param.IDENTIFIER().getText()
            param_type = self.cast_to_python_type(param.data_type().getText())
            params_with_types.append(f"{param_name}: {param_type}")

        params = ", ".join(params_with_types)

        if ctx.RETURNS():
            return_type = self.cast_to_python_type(ctx.data_type().getText())
        else:
            return_type = None

        self.indent_level += 1
        body = "\n".join(
            [
                self.indent() + self.visit(stmt)
                for stmt in ctx.statement_list().statement()
            ]
        )
        self.indent_level -= 1

        if return_type:
            return f"def {func_name}({params}) -> {return_type}:\n{body}"
        else:
            return f"def {func_name}({params}):\n{body}"

    def visitParameter(self, ctx):

        param_name = ctx.IDENTIFIER().getText()
        return param_name

    def visitFile_handling(self, ctx):
        file_handler = (
            ctx.STRING_LITERAL().getText().lower().replace('"', "").split(".")[0]
        )
        if ctx.OPENFILE():
            file_mode = "w" if ctx.file_mode().getText() == "WRITE" else "r"

            return f"{file_handler} = open({ctx.STRING_LITERAL()}, mode='{file_mode}')"

        if ctx.READFILE():
            return f"{ctx.IDENTIFIER()} = {file_handler}.read()"

        if ctx.WRITEFILE():
            return f"{file_handler}.write({ctx.IDENTIFIER()})"

        if ctx.CLOSEFILE():
            return f"{file_handler}.close()"


def translate_pseudocode_to_python(input_file, output_file):
    input_stream = FileStream('input_files/' + input_file, encoding="utf-8")
    lexer = PseudoCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PseudoCodeParser(token_stream)
    tree = parser.program()

    visitor = PseudoCodeToPythonVisitor()
    python_code = visitor.visit(tree)

    with open('output_files/' + output_file, "w") as f:
        f.write(python_code)

    try:
        black.format_file_in_place(
            src=black.Path('output_files/' + output_file),
            fast=False,
            mode=black.FileMode(),
            write_back=black.WriteBack.YES,
        )
        print(f"File {output_file} has been formatted using Black.")
    except Exception as e:
        print(f"Failed to format the file {output_file}: {e}")


def main(input_file='test.pseudo', output_file='test.py', run_script=False):
    if input_file and output_file:

        translate_pseudocode_to_python(input_file=input_file, output_file=output_file)
        if run_script:
            try:
                subprocess.run(["python", output_file], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while executing the compiled script: {e}")
    else:

        parser = argparse.ArgumentParser(description="Translate pseudocode to Python.")
        parser.add_argument("--file", required=True, help="Path to the input pseudocode script.")
        parser.add_argument("--output", default="output_files/output.py", help="Path to save the compiled Python script.")
        parser.add_argument("--run", action="store_true", help="Execute the compiled script after compilation.")

        args = parser.parse_args()

        translate_pseudocode_to_python(input_file=args.file, output_file=args.output)

        if args.run:
            try:
                subprocess.run(["python", args.output], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while executing the compiled script: {e}")


if __name__ == "__main__":
    main()

