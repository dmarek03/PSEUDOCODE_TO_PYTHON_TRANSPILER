# Generated from PseudoCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudoCodeParser import PseudoCodeParser
else:
    from PseudoCodeParser import PseudoCodeParser

# This class defines a complete listener for a parse tree produced by PseudoCodeParser.
class PseudoCodeListener(ParseTreeListener):

    # Enter a parse tree produced by PseudoCodeParser#program.
    def enterProgram(self, ctx:PseudoCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#program.
    def exitProgram(self, ctx:PseudoCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#statement_list.
    def enterStatement_list(self, ctx:PseudoCodeParser.Statement_listContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#statement_list.
    def exitStatement_list(self, ctx:PseudoCodeParser.Statement_listContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#statement.
    def enterStatement(self, ctx:PseudoCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#statement.
    def exitStatement(self, ctx:PseudoCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#return_statement.
    def enterReturn_statement(self, ctx:PseudoCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#return_statement.
    def exitReturn_statement(self, ctx:PseudoCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#comment_statement.
    def enterComment_statement(self, ctx:PseudoCodeParser.Comment_statementContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#comment_statement.
    def exitComment_statement(self, ctx:PseudoCodeParser.Comment_statementContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#declaration.
    def enterDeclaration(self, ctx:PseudoCodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#declaration.
    def exitDeclaration(self, ctx:PseudoCodeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#data_type.
    def enterData_type(self, ctx:PseudoCodeParser.Data_typeContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#data_type.
    def exitData_type(self, ctx:PseudoCodeParser.Data_typeContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#index_type.
    def enterIndex_type(self, ctx:PseudoCodeParser.Index_typeContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#index_type.
    def exitIndex_type(self, ctx:PseudoCodeParser.Index_typeContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#assignment.
    def enterAssignment(self, ctx:PseudoCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#assignment.
    def exitAssignment(self, ctx:PseudoCodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#cast.
    def enterCast(self, ctx:PseudoCodeParser.CastContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#cast.
    def exitCast(self, ctx:PseudoCodeParser.CastContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#type.
    def enterType(self, ctx:PseudoCodeParser.TypeContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#type.
    def exitType(self, ctx:PseudoCodeParser.TypeContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#expression.
    def enterExpression(self, ctx:PseudoCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#expression.
    def exitExpression(self, ctx:PseudoCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#additionExpression.
    def enterAdditionExpression(self, ctx:PseudoCodeParser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#additionExpression.
    def exitAdditionExpression(self, ctx:PseudoCodeParser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:PseudoCodeParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:PseudoCodeParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:PseudoCodeParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:PseudoCodeParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#term.
    def enterTerm(self, ctx:PseudoCodeParser.TermContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#term.
    def exitTerm(self, ctx:PseudoCodeParser.TermContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#literal.
    def enterLiteral(self, ctx:PseudoCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#literal.
    def exitLiteral(self, ctx:PseudoCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#input.
    def enterInput(self, ctx:PseudoCodeParser.InputContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#input.
    def exitInput(self, ctx:PseudoCodeParser.InputContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#output.
    def enterOutput(self, ctx:PseudoCodeParser.OutputContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#output.
    def exitOutput(self, ctx:PseudoCodeParser.OutputContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#value_list.
    def enterValue_list(self, ctx:PseudoCodeParser.Value_listContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#value_list.
    def exitValue_list(self, ctx:PseudoCodeParser.Value_listContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#if_statement.
    def enterIf_statement(self, ctx:PseudoCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#if_statement.
    def exitIf_statement(self, ctx:PseudoCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#condition.
    def enterCondition(self, ctx:PseudoCodeParser.ConditionContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#condition.
    def exitCondition(self, ctx:PseudoCodeParser.ConditionContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#comparison_operator.
    def enterComparison_operator(self, ctx:PseudoCodeParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#comparison_operator.
    def exitComparison_operator(self, ctx:PseudoCodeParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#case_statement.
    def enterCase_statement(self, ctx:PseudoCodeParser.Case_statementContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#case_statement.
    def exitCase_statement(self, ctx:PseudoCodeParser.Case_statementContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#case_list.
    def enterCase_list(self, ctx:PseudoCodeParser.Case_listContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#case_list.
    def exitCase_list(self, ctx:PseudoCodeParser.Case_listContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#case.
    def enterCase(self, ctx:PseudoCodeParser.CaseContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#case.
    def exitCase(self, ctx:PseudoCodeParser.CaseContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#while_loop.
    def enterWhile_loop(self, ctx:PseudoCodeParser.While_loopContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#while_loop.
    def exitWhile_loop(self, ctx:PseudoCodeParser.While_loopContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#for_loop.
    def enterFor_loop(self, ctx:PseudoCodeParser.For_loopContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#for_loop.
    def exitFor_loop(self, ctx:PseudoCodeParser.For_loopContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#repeat_until_loop.
    def enterRepeat_until_loop(self, ctx:PseudoCodeParser.Repeat_until_loopContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#repeat_until_loop.
    def exitRepeat_until_loop(self, ctx:PseudoCodeParser.Repeat_until_loopContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#procedure_call.
    def enterProcedure_call(self, ctx:PseudoCodeParser.Procedure_callContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#procedure_call.
    def exitProcedure_call(self, ctx:PseudoCodeParser.Procedure_callContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#user_function_definition.
    def enterUser_function_definition(self, ctx:PseudoCodeParser.User_function_definitionContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#user_function_definition.
    def exitUser_function_definition(self, ctx:PseudoCodeParser.User_function_definitionContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#parameter_list.
    def enterParameter_list(self, ctx:PseudoCodeParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#parameter_list.
    def exitParameter_list(self, ctx:PseudoCodeParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#parameter.
    def enterParameter(self, ctx:PseudoCodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#parameter.
    def exitParameter(self, ctx:PseudoCodeParser.ParameterContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#function_call.
    def enterFunction_call(self, ctx:PseudoCodeParser.Function_callContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#function_call.
    def exitFunction_call(self, ctx:PseudoCodeParser.Function_callContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#user_function_call.
    def enterUser_function_call(self, ctx:PseudoCodeParser.User_function_callContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#user_function_call.
    def exitUser_function_call(self, ctx:PseudoCodeParser.User_function_callContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#argument_list.
    def enterArgument_list(self, ctx:PseudoCodeParser.Argument_listContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#argument_list.
    def exitArgument_list(self, ctx:PseudoCodeParser.Argument_listContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#builtin_function_call.
    def enterBuiltin_function_call(self, ctx:PseudoCodeParser.Builtin_function_callContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#builtin_function_call.
    def exitBuiltin_function_call(self, ctx:PseudoCodeParser.Builtin_function_callContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#file_handling.
    def enterFile_handling(self, ctx:PseudoCodeParser.File_handlingContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#file_handling.
    def exitFile_handling(self, ctx:PseudoCodeParser.File_handlingContext):
        pass


    # Enter a parse tree produced by PseudoCodeParser#file_mode.
    def enterFile_mode(self, ctx:PseudoCodeParser.File_modeContext):
        pass

    # Exit a parse tree produced by PseudoCodeParser#file_mode.
    def exitFile_mode(self, ctx:PseudoCodeParser.File_modeContext):
        pass



del PseudoCodeParser