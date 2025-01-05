# Generated from PseudoCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudoCodeParser import PseudoCodeParser
else:
    from PseudoCodeParser import PseudoCodeParser

# This class defines a complete generic visitor for a parse tree produced by PseudoCodeParser.

class PseudoCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PseudoCodeParser#program.
    def visitProgram(self, ctx:PseudoCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#statement_list.
    def visitStatement_list(self, ctx:PseudoCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#statement.
    def visitStatement(self, ctx:PseudoCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#return_statement.
    def visitReturn_statement(self, ctx:PseudoCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#comment_statement.
    def visitComment_statement(self, ctx:PseudoCodeParser.Comment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#declaration.
    def visitDeclaration(self, ctx:PseudoCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#data_type.
    def visitData_type(self, ctx:PseudoCodeParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#index_type.
    def visitIndex_type(self, ctx:PseudoCodeParser.Index_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#assignment.
    def visitAssignment(self, ctx:PseudoCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#cast.
    def visitCast(self, ctx:PseudoCodeParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#type.
    def visitType(self, ctx:PseudoCodeParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#expression.
    def visitExpression(self, ctx:PseudoCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#additionExpression.
    def visitAdditionExpression(self, ctx:PseudoCodeParser.AdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#multiplicationExpression.
    def visitMultiplicationExpression(self, ctx:PseudoCodeParser.MultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:PseudoCodeParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#term.
    def visitTerm(self, ctx:PseudoCodeParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#literal.
    def visitLiteral(self, ctx:PseudoCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#input.
    def visitInput(self, ctx:PseudoCodeParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#output.
    def visitOutput(self, ctx:PseudoCodeParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#value_list.
    def visitValue_list(self, ctx:PseudoCodeParser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#if_statement.
    def visitIf_statement(self, ctx:PseudoCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#condition.
    def visitCondition(self, ctx:PseudoCodeParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#comparison_operator.
    def visitComparison_operator(self, ctx:PseudoCodeParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#case_statement.
    def visitCase_statement(self, ctx:PseudoCodeParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#case_list.
    def visitCase_list(self, ctx:PseudoCodeParser.Case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#case.
    def visitCase(self, ctx:PseudoCodeParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#while_loop.
    def visitWhile_loop(self, ctx:PseudoCodeParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#for_loop.
    def visitFor_loop(self, ctx:PseudoCodeParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#repeat_until_loop.
    def visitRepeat_until_loop(self, ctx:PseudoCodeParser.Repeat_until_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#procedure_call.
    def visitProcedure_call(self, ctx:PseudoCodeParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#user_function_definition.
    def visitUser_function_definition(self, ctx:PseudoCodeParser.User_function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#parameter_list.
    def visitParameter_list(self, ctx:PseudoCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#parameter.
    def visitParameter(self, ctx:PseudoCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#function_call.
    def visitFunction_call(self, ctx:PseudoCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#user_function_call.
    def visitUser_function_call(self, ctx:PseudoCodeParser.User_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#argument_list.
    def visitArgument_list(self, ctx:PseudoCodeParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#builtin_function_call.
    def visitBuiltin_function_call(self, ctx:PseudoCodeParser.Builtin_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#file_handling.
    def visitFile_handling(self, ctx:PseudoCodeParser.File_handlingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeParser#file_mode.
    def visitFile_mode(self, ctx:PseudoCodeParser.File_modeContext):
        return self.visitChildren(ctx)



del PseudoCodeParser