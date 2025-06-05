# Generated from ASICParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ASICParser import ASICParser
else:
    from ASICParser import ASICParser

# This class defines a complete generic visitor for a parse tree produced by ASICParser.

class ASICParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ASICParser#prog.
    def visitProg(self, ctx:ASICParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#line.
    def visitLine(self, ctx:ASICParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#definition.
    def visitDefinition(self, ctx:ASICParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#define_def.
    def visitDefine_def(self, ctx:ASICParser.Define_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#config_def.
    def visitConfig_def(self, ctx:ASICParser.Config_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#const_def.
    def visitConst_def(self, ctx:ASICParser.Const_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#constant.
    def visitConstant(self, ctx:ASICParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#statement.
    def visitStatement(self, ctx:ASICParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#instruction.
    def visitInstruction(self, ctx:ASICParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#sregop.
    def visitSregop(self, ctx:ASICParser.SregopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#asignment.
    def visitAsignment(self, ctx:ASICParser.AsignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#arith.
    def visitArith(self, ctx:ASICParser.ArithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#AluSpOp.
    def visitAluSpOp(self, ctx:ASICParser.AluSpOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#SpCopOp.
    def visitSpCopOp(self, ctx:ASICParser.SpCopOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#SpCopOnly.
    def visitSpCopOnly(self, ctx:ASICParser.SpCopOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#lbl.
    def visitLbl(self, ctx:ASICParser.LblContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#label.
    def visitLabel(self, ctx:ASICParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#primary_expression.
    def visitPrimary_expression(self, ctx:ASICParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#unary_expression.
    def visitUnary_expression(self, ctx:ASICParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#unary_operator.
    def visitUnary_operator(self, ctx:ASICParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#mulop.
    def visitMulop(self, ctx:ASICParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:ASICParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#addop.
    def visitAddop(self, ctx:ASICParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#additive_expression.
    def visitAdditive_expression(self, ctx:ASICParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#relop.
    def visitRelop(self, ctx:ASICParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#relational_expression.
    def visitRelational_expression(self, ctx:ASICParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#eqop.
    def visitEqop(self, ctx:ASICParser.EqopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#equality_expression.
    def visitEquality_expression(self, ctx:ASICParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#and_expression.
    def visitAnd_expression(self, ctx:ASICParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#xor_expression.
    def visitXor_expression(self, ctx:ASICParser.Xor_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#or_expression.
    def visitOr_expression(self, ctx:ASICParser.Or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#logicaland_expression.
    def visitLogicaland_expression(self, ctx:ASICParser.Logicaland_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#logicalor_expression.
    def visitLogicalor_expression(self, ctx:ASICParser.Logicalor_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#expression.
    def visitExpression(self, ctx:ASICParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#rev_configuration.
    def visitRev_configuration(self, ctx:ASICParser.Rev_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#configuration.
    def visitConfiguration(self, ctx:ASICParser.ConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#conf_atom.
    def visitConf_atom(self, ctx:ASICParser.Conf_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#conf_d.
    def visitConf_d(self, ctx:ASICParser.Conf_dContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#conf_c.
    def visitConf_c(self, ctx:ASICParser.Conf_cContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#const_expr.
    def visitConst_expr(self, ctx:ASICParser.Const_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#op.
    def visitOp(self, ctx:ASICParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#define_name.
    def visitDefine_name(self, ctx:ASICParser.Define_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#config_name.
    def visitConfig_name(self, ctx:ASICParser.Config_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#const_name.
    def visitConst_name(self, ctx:ASICParser.Const_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#argument.
    def visitArgument(self, ctx:ASICParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#resultexpr.
    def visitResultexpr(self, ctx:ASICParser.ResultexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#sreg.
    def visitSreg(self, ctx:ASICParser.SregContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#arg.
    def visitArg(self, ctx:ASICParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#vreg.
    def visitVreg(self, ctx:ASICParser.VregContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#vreg_r.
    def visitVreg_r(self, ctx:ASICParser.Vreg_rContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#output.
    def visitOutput(self, ctx:ASICParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#stdop.
    def visitStdop(self, ctx:ASICParser.StdopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#aluop.
    def visitAluop(self, ctx:ASICParser.AluopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#spcop.
    def visitSpcop(self, ctx:ASICParser.SpcopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASICParser#comment.
    def visitComment(self, ctx:ASICParser.CommentContext):
        return self.visitChildren(ctx)



del ASICParser