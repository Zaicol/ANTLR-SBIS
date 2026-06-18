from typing import Any

from generated.ASICLexer import ASICLexer
from generated.ASICParserVisitor import ASICParserVisitor
from generated.ASICParser import ASICParser
from models.exceptions.AssemblerError import AssemblerError
from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError
from models.exceptions.BitValueError import BitValueError


class ExpressionEvaluator(ASICParserVisitor):
    defines: dict[str, Any]
    line: int

    def __init__(self, defines, line):
        self.defines = defines
        self.line = line

    def visit_line(self, ctx, line):
        self.line = line
        res = super().visit(ctx)
        print("result:", res)
        if not (0 <= res <= 255):
            raise BitValueError(f"Константа {res} не помещается в 8 бит (допустимый диапазон: 0–255)")

        return res

    def visitExpression(self, ctx: ASICParser.ExpressionContext):
        if ctx.constant():
            return self.visit(ctx.constant())

        return self.visit(ctx.logicalor_expression())

    def visitUnary_expression(self, ctx: ASICParser.Unary_expressionContext):
        if ctx.primary_expression():
            return self.visit(ctx.primary_expression())

        value = self.visit(ctx.unary_expression())
        oper = ctx.unary_operator().getText()

        if oper == '+':
            return value

        if oper == '-':
            return -value

        if oper == '~':
            return ~value

        if oper.lower() == 'neg':
            return int(not value)

        raise AssemblerSyntaxError(f"Unknown unary operator: {oper}", self.line)

    def visitMultiplicative_expression(self, ctx: ASICParser.Multiplicative_expressionContext):
        result = self.visit(ctx.unary_expression(0))

        for i, op_ctx in enumerate(ctx.mulop()):
            right = self.visit(ctx.unary_expression(i + 1))
            oper = op_ctx.getText()

            if oper == '*':
                result *= right

            elif oper == '/':
                result //= right

            elif oper == '%':
                result %= right

            else:
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.line
                )

        return result

    def visitAdditive_expression(self, ctx: ASICParser.Additive_expressionContext):
        result = self.visit(ctx.multiplicative_expression(0))

        for i, op_ctx in enumerate(ctx.addop()):
            right = self.visit(ctx.multiplicative_expression(i + 1))
            oper = op_ctx.getText()

            if oper == '+':
                result += right

            elif oper == '-':
                result -= right

            else:
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.line
                )

        return result

    def visitRelational_expression(self, ctx: ASICParser.Relational_expressionContext):
        result = self.visit(ctx.additive_expression(0))

        for i, op_ctx in enumerate(ctx.relop()):
            right = self.visit(ctx.additive_expression(i + 1))
            oper = op_ctx.getText()

            if oper == '<':
                result = int(result < right)

            elif oper == '>':
                result = int(result > right)

            elif oper == '<=':
                result = int(result <= right)

            elif oper == '>=':
                result = int(result >= right)

            else:
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.line
                )

        return result

    def visitEquality_expression(self, ctx: ASICParser.Equality_expressionContext):
        result = self.visit(ctx.relational_expression(0))

        for i, op_ctx in enumerate(ctx.eqop()):
            right = self.visit(ctx.relational_expression(i + 1))
            oper = op_ctx.getText()

            if oper == '==':
                result = int(result == right)

            elif oper == '!=':
                result = int(result != right)

            else:
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.line
                )

        return result

    def visitAnd_expression(self, ctx: ASICParser.And_expressionContext):
        result = self.visit(ctx.equality_expression(0))

        for i in range(1, len(ctx.equality_expression())):
            result &= self.visit(ctx.equality_expression(i))

        return result

    def visitXor_expression(self, ctx: ASICParser.Xor_expressionContext):
        result = self.visit(ctx.and_expression(0))

        for i in range(1, len(ctx.and_expression())):
            result ^= self.visit(ctx.and_expression(i))

        return result

    def visitOr_expression(self, ctx: ASICParser.Or_expressionContext):
        result = self.visit(ctx.xor_expression(0))

        for i in range(1, len(ctx.xor_expression())):
            result |= self.visit(ctx.xor_expression(i))

        return result

    def visitLogicaland_expression(self, ctx: ASICParser.Logicaland_expressionContext):
        result = self.visit(ctx.or_expression(0))

        for i in range(1, len(ctx.or_expression())):
            result = int(
                bool(result)
                and
                bool(self.visit(ctx.or_expression(i)))
            )

        return result

    def visitLogicalor_expression(self, ctx: ASICParser.Logicalor_expressionContext):
        result = self.visit(ctx.logicaland_expression(0))

        for i in range(1, len(ctx.logicaland_expression())):
            result = int(
                bool(result)
                or
                bool(self.visit(ctx.logicaland_expression(i)))
            )

        return result

    def visitDefine_name(self, ctx: ASICParser.Define_nameContext):
        if not ctx.getText() in self.defines:
            raise AssemblerSyntaxError("Unknown define: " + ctx.getText(), self.line)
        try:
            return int(self.defines[ctx.getText()])
        except ValueError:
            raise AssemblerSyntaxError("Not-integer define: " + ctx.getText(), self.line)

    def visitConstant(self, ctx: ASICParser.ConstantContext):
        token = ctx.getChild(0).getSymbol()
        token_type = token.type
        text = ctx.getText()
        text_up = text.upper()

        if token_type == ASICLexer.HEXADECIMAL:
            if text_up.endswith('H'):
                num_part = text[:-1]
            else:  # начинается с 0x или 0X
                num_part = text[2:]
            value = int(num_part, 16)

        elif token_type == ASICLexer.BINARY:
            if text_up.endswith('B'):
                num_part = text[:-1]
            else:  # начинается с 0b или 0B
                num_part = text[2:]
            value = int(num_part, 2)

        elif token_type == ASICLexer.OCTAL:
            if text_up.endswith('O'):
                num_part = text[:-1]
            else:  # начинается с 0o или 0O
                num_part = text[2:]
            value = int(num_part, 8)

        elif token_type == ASICLexer.DECIMAL:
            if text_up.endswith('D'):
                num_part = text[:-1]
            elif text_up.startswith('0D'):
                num_part = text[2:]
            else:
                num_part = text
            value = int(num_part, 10)

        else:
            raise AssemblerError(f"Неизвестный тип константы: {text}")

        return value

    def visit_if_not_null(self, expr):
        if expr is None:
            return None
        return self.visit(expr)
