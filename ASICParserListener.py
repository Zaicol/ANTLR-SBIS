# Generated from ASICParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ASICParser import ASICParser
else:
    from ASICParser import ASICParser

# This class defines a complete listener for a parse tree produced by ASICParser.
class ASICParserListener(ParseTreeListener):

    # Enter a parse tree produced by ASICParser#prog.
    def enterProg(self, ctx:ASICParser.ProgContext):
        pass

    # Exit a parse tree produced by ASICParser#prog.
    def exitProg(self, ctx:ASICParser.ProgContext):
        pass


    # Enter a parse tree produced by ASICParser#line.
    def enterLine(self, ctx:ASICParser.LineContext):
        pass

    # Exit a parse tree produced by ASICParser#line.
    def exitLine(self, ctx:ASICParser.LineContext):
        pass


    # Enter a parse tree produced by ASICParser#definition.
    def enterDefinition(self, ctx:ASICParser.DefinitionContext):
        pass

    # Exit a parse tree produced by ASICParser#definition.
    def exitDefinition(self, ctx:ASICParser.DefinitionContext):
        pass


    # Enter a parse tree produced by ASICParser#define_def.
    def enterDefine_def(self, ctx:ASICParser.Define_defContext):
        pass

    # Exit a parse tree produced by ASICParser#define_def.
    def exitDefine_def(self, ctx:ASICParser.Define_defContext):
        pass


    # Enter a parse tree produced by ASICParser#config_def.
    def enterConfig_def(self, ctx:ASICParser.Config_defContext):
        pass

    # Exit a parse tree produced by ASICParser#config_def.
    def exitConfig_def(self, ctx:ASICParser.Config_defContext):
        pass


    # Enter a parse tree produced by ASICParser#const_def.
    def enterConst_def(self, ctx:ASICParser.Const_defContext):
        pass

    # Exit a parse tree produced by ASICParser#const_def.
    def exitConst_def(self, ctx:ASICParser.Const_defContext):
        pass


    # Enter a parse tree produced by ASICParser#constant.
    def enterConstant(self, ctx:ASICParser.ConstantContext):
        pass

    # Exit a parse tree produced by ASICParser#constant.
    def exitConstant(self, ctx:ASICParser.ConstantContext):
        pass


    # Enter a parse tree produced by ASICParser#statement.
    def enterStatement(self, ctx:ASICParser.StatementContext):
        pass

    # Exit a parse tree produced by ASICParser#statement.
    def exitStatement(self, ctx:ASICParser.StatementContext):
        pass


    # Enter a parse tree produced by ASICParser#instruction.
    def enterInstruction(self, ctx:ASICParser.InstructionContext):
        pass

    # Exit a parse tree produced by ASICParser#instruction.
    def exitInstruction(self, ctx:ASICParser.InstructionContext):
        pass


    # Enter a parse tree produced by ASICParser#sregop.
    def enterSregop(self, ctx:ASICParser.SregopContext):
        pass

    # Exit a parse tree produced by ASICParser#sregop.
    def exitSregop(self, ctx:ASICParser.SregopContext):
        pass


    # Enter a parse tree produced by ASICParser#asignment.
    def enterAsignment(self, ctx:ASICParser.AsignmentContext):
        pass

    # Exit a parse tree produced by ASICParser#asignment.
    def exitAsignment(self, ctx:ASICParser.AsignmentContext):
        pass


    # Enter a parse tree produced by ASICParser#arith.
    def enterArith(self, ctx:ASICParser.ArithContext):
        pass

    # Exit a parse tree produced by ASICParser#arith.
    def exitArith(self, ctx:ASICParser.ArithContext):
        pass


    # Enter a parse tree produced by ASICParser#AluSpOp.
    def enterAluSpOp(self, ctx:ASICParser.AluSpOpContext):
        pass

    # Exit a parse tree produced by ASICParser#AluSpOp.
    def exitAluSpOp(self, ctx:ASICParser.AluSpOpContext):
        pass


    # Enter a parse tree produced by ASICParser#SpCopOp.
    def enterSpCopOp(self, ctx:ASICParser.SpCopOpContext):
        pass

    # Exit a parse tree produced by ASICParser#SpCopOp.
    def exitSpCopOp(self, ctx:ASICParser.SpCopOpContext):
        pass


    # Enter a parse tree produced by ASICParser#SpCopOnly.
    def enterSpCopOnly(self, ctx:ASICParser.SpCopOnlyContext):
        pass

    # Exit a parse tree produced by ASICParser#SpCopOnly.
    def exitSpCopOnly(self, ctx:ASICParser.SpCopOnlyContext):
        pass


    # Enter a parse tree produced by ASICParser#lbl.
    def enterLbl(self, ctx:ASICParser.LblContext):
        pass

    # Exit a parse tree produced by ASICParser#lbl.
    def exitLbl(self, ctx:ASICParser.LblContext):
        pass


    # Enter a parse tree produced by ASICParser#label.
    def enterLabel(self, ctx:ASICParser.LabelContext):
        pass

    # Exit a parse tree produced by ASICParser#label.
    def exitLabel(self, ctx:ASICParser.LabelContext):
        pass


    # Enter a parse tree produced by ASICParser#primary_expression.
    def enterPrimary_expression(self, ctx:ASICParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#primary_expression.
    def exitPrimary_expression(self, ctx:ASICParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#unary_expression.
    def enterUnary_expression(self, ctx:ASICParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#unary_expression.
    def exitUnary_expression(self, ctx:ASICParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#unary_operator.
    def enterUnary_operator(self, ctx:ASICParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by ASICParser#unary_operator.
    def exitUnary_operator(self, ctx:ASICParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by ASICParser#mulop.
    def enterMulop(self, ctx:ASICParser.MulopContext):
        pass

    # Exit a parse tree produced by ASICParser#mulop.
    def exitMulop(self, ctx:ASICParser.MulopContext):
        pass


    # Enter a parse tree produced by ASICParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:ASICParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:ASICParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#addop.
    def enterAddop(self, ctx:ASICParser.AddopContext):
        pass

    # Exit a parse tree produced by ASICParser#addop.
    def exitAddop(self, ctx:ASICParser.AddopContext):
        pass


    # Enter a parse tree produced by ASICParser#additive_expression.
    def enterAdditive_expression(self, ctx:ASICParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#additive_expression.
    def exitAdditive_expression(self, ctx:ASICParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#relop.
    def enterRelop(self, ctx:ASICParser.RelopContext):
        pass

    # Exit a parse tree produced by ASICParser#relop.
    def exitRelop(self, ctx:ASICParser.RelopContext):
        pass


    # Enter a parse tree produced by ASICParser#relational_expression.
    def enterRelational_expression(self, ctx:ASICParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#relational_expression.
    def exitRelational_expression(self, ctx:ASICParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#eqop.
    def enterEqop(self, ctx:ASICParser.EqopContext):
        pass

    # Exit a parse tree produced by ASICParser#eqop.
    def exitEqop(self, ctx:ASICParser.EqopContext):
        pass


    # Enter a parse tree produced by ASICParser#equality_expression.
    def enterEquality_expression(self, ctx:ASICParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#equality_expression.
    def exitEquality_expression(self, ctx:ASICParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#and_expression.
    def enterAnd_expression(self, ctx:ASICParser.And_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#and_expression.
    def exitAnd_expression(self, ctx:ASICParser.And_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#xor_expression.
    def enterXor_expression(self, ctx:ASICParser.Xor_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#xor_expression.
    def exitXor_expression(self, ctx:ASICParser.Xor_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#or_expression.
    def enterOr_expression(self, ctx:ASICParser.Or_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#or_expression.
    def exitOr_expression(self, ctx:ASICParser.Or_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#logicaland_expression.
    def enterLogicaland_expression(self, ctx:ASICParser.Logicaland_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#logicaland_expression.
    def exitLogicaland_expression(self, ctx:ASICParser.Logicaland_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#logicalor_expression.
    def enterLogicalor_expression(self, ctx:ASICParser.Logicalor_expressionContext):
        pass

    # Exit a parse tree produced by ASICParser#logicalor_expression.
    def exitLogicalor_expression(self, ctx:ASICParser.Logicalor_expressionContext):
        pass


    # Enter a parse tree produced by ASICParser#expression.
    def enterExpression(self, ctx:ASICParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ASICParser#expression.
    def exitExpression(self, ctx:ASICParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ASICParser#rev_configuration.
    def enterRev_configuration(self, ctx:ASICParser.Rev_configurationContext):
        pass

    # Exit a parse tree produced by ASICParser#rev_configuration.
    def exitRev_configuration(self, ctx:ASICParser.Rev_configurationContext):
        pass


    # Enter a parse tree produced by ASICParser#configuration.
    def enterConfiguration(self, ctx:ASICParser.ConfigurationContext):
        pass

    # Exit a parse tree produced by ASICParser#configuration.
    def exitConfiguration(self, ctx:ASICParser.ConfigurationContext):
        pass


    # Enter a parse tree produced by ASICParser#conf_atom.
    def enterConf_atom(self, ctx:ASICParser.Conf_atomContext):
        pass

    # Exit a parse tree produced by ASICParser#conf_atom.
    def exitConf_atom(self, ctx:ASICParser.Conf_atomContext):
        pass


    # Enter a parse tree produced by ASICParser#conf_d.
    def enterConf_d(self, ctx:ASICParser.Conf_dContext):
        pass

    # Exit a parse tree produced by ASICParser#conf_d.
    def exitConf_d(self, ctx:ASICParser.Conf_dContext):
        pass


    # Enter a parse tree produced by ASICParser#conf_c.
    def enterConf_c(self, ctx:ASICParser.Conf_cContext):
        pass

    # Exit a parse tree produced by ASICParser#conf_c.
    def exitConf_c(self, ctx:ASICParser.Conf_cContext):
        pass


    # Enter a parse tree produced by ASICParser#const_expr.
    def enterConst_expr(self, ctx:ASICParser.Const_exprContext):
        pass

    # Exit a parse tree produced by ASICParser#const_expr.
    def exitConst_expr(self, ctx:ASICParser.Const_exprContext):
        pass


    # Enter a parse tree produced by ASICParser#op.
    def enterOp(self, ctx:ASICParser.OpContext):
        pass

    # Exit a parse tree produced by ASICParser#op.
    def exitOp(self, ctx:ASICParser.OpContext):
        pass


    # Enter a parse tree produced by ASICParser#define_name.
    def enterDefine_name(self, ctx:ASICParser.Define_nameContext):
        pass

    # Exit a parse tree produced by ASICParser#define_name.
    def exitDefine_name(self, ctx:ASICParser.Define_nameContext):
        pass


    # Enter a parse tree produced by ASICParser#config_name.
    def enterConfig_name(self, ctx:ASICParser.Config_nameContext):
        pass

    # Exit a parse tree produced by ASICParser#config_name.
    def exitConfig_name(self, ctx:ASICParser.Config_nameContext):
        pass


    # Enter a parse tree produced by ASICParser#const_name.
    def enterConst_name(self, ctx:ASICParser.Const_nameContext):
        pass

    # Exit a parse tree produced by ASICParser#const_name.
    def exitConst_name(self, ctx:ASICParser.Const_nameContext):
        pass


    # Enter a parse tree produced by ASICParser#argument.
    def enterArgument(self, ctx:ASICParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ASICParser#argument.
    def exitArgument(self, ctx:ASICParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ASICParser#resultexpr.
    def enterResultexpr(self, ctx:ASICParser.ResultexprContext):
        pass

    # Exit a parse tree produced by ASICParser#resultexpr.
    def exitResultexpr(self, ctx:ASICParser.ResultexprContext):
        pass


    # Enter a parse tree produced by ASICParser#sreg.
    def enterSreg(self, ctx:ASICParser.SregContext):
        pass

    # Exit a parse tree produced by ASICParser#sreg.
    def exitSreg(self, ctx:ASICParser.SregContext):
        pass


    # Enter a parse tree produced by ASICParser#arg.
    def enterArg(self, ctx:ASICParser.ArgContext):
        pass

    # Exit a parse tree produced by ASICParser#arg.
    def exitArg(self, ctx:ASICParser.ArgContext):
        pass


    # Enter a parse tree produced by ASICParser#vreg.
    def enterVreg(self, ctx:ASICParser.VregContext):
        pass

    # Exit a parse tree produced by ASICParser#vreg.
    def exitVreg(self, ctx:ASICParser.VregContext):
        pass


    # Enter a parse tree produced by ASICParser#vreg_r.
    def enterVreg_r(self, ctx:ASICParser.Vreg_rContext):
        pass

    # Exit a parse tree produced by ASICParser#vreg_r.
    def exitVreg_r(self, ctx:ASICParser.Vreg_rContext):
        pass


    # Enter a parse tree produced by ASICParser#output.
    def enterOutput(self, ctx:ASICParser.OutputContext):
        pass

    # Exit a parse tree produced by ASICParser#output.
    def exitOutput(self, ctx:ASICParser.OutputContext):
        pass


    # Enter a parse tree produced by ASICParser#stdop.
    def enterStdop(self, ctx:ASICParser.StdopContext):
        pass

    # Exit a parse tree produced by ASICParser#stdop.
    def exitStdop(self, ctx:ASICParser.StdopContext):
        pass


    # Enter a parse tree produced by ASICParser#aluop.
    def enterAluop(self, ctx:ASICParser.AluopContext):
        pass

    # Exit a parse tree produced by ASICParser#aluop.
    def exitAluop(self, ctx:ASICParser.AluopContext):
        pass


    # Enter a parse tree produced by ASICParser#spcop.
    def enterSpcop(self, ctx:ASICParser.SpcopContext):
        pass

    # Exit a parse tree produced by ASICParser#spcop.
    def exitSpcop(self, ctx:ASICParser.SpcopContext):
        pass


    # Enter a parse tree produced by ASICParser#comment.
    def enterComment(self, ctx:ASICParser.CommentContext):
        pass

    # Exit a parse tree produced by ASICParser#comment.
    def exitComment(self, ctx:ASICParser.CommentContext):
        pass



del ASICParser