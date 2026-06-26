from typing import Any

from generated.ASICLexer import ASICLexer
from generated.ASICParserVisitor import ASICParserVisitor
from generated.ASICParser import ASICParser
from models.Label import Label
from models.exceptions.AssemblerError import AssemblerError
from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError
from models.exceptions.BitValueError import BitValueError


class ExpressionEvaluator(ASICParserVisitor):
    defines: dict[str, int]
    labels: dict[str, Label]
    source_line: int

    def __init__(self, defines, labels=None):
        self.defines = {}
        self.labels = labels
        for name, define in defines.items():
            self.defines[name] = self.visit(define)
        self.source_line = 0

    def visit_line(self, ctx: ASICParser.ExpressionContext, max_size_in_bits: int = 8) -> int:
        self.source_line = ctx.start.line
        res = super().visit(ctx)
        column: int = ctx.start.column
        max_size = (2 ** max_size_in_bits) - 1
        if not (0 <= res <= max_size):
            raise BitValueError(f"Expression value {res} out of range [0, {max_size}]",
                                self.source_line, column)

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

        if oper == '!':
            return not value

        column: int = ctx.start.column
        raise AssemblerSyntaxError(f"Unknown unary operator: {oper}", self.source_line, column)

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
                    self.source_line
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
                column: int = ctx.start.column
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.source_line,
                    column
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
                column: int = ctx.start.column
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.source_line,
                    column
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
                column: int = ctx.start.column
                raise AssemblerSyntaxError(
                    f"Unknown operator: {oper}",
                    self.source_line,
                    column
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
        if ctx.getText() in self.defines:
            try:
                return int(self.defines[ctx.getText()])
            except ValueError:
                raise AssemblerSyntaxError("Not-integer define: " + ctx.getText(), self.source_line, ctx.start.column)
        if self.labels is not None and ctx.getText() in self.labels:
            try:
                return self.labels[ctx.getText()].source_line
            except ValueError:
                raise AssemblerSyntaxError("Couldn't find label: " + ctx.getText(), self.source_line, ctx.start.column)
        raise AssemblerSyntaxError("Unknown define: " + ctx.getText(), self.source_line, ctx.start.column)

    def visitConstant(self, ctx: ASICParser.ConstantContext):
        token = ctx.getChild(0).getSymbol()
        text = ctx.getText()

        rules = {
            # token.type: (base, prefix, suffix)
            ASICLexer.BINARY: (2, "0B", "B"),
            ASICLexer.OCTAL: (8, "0O", "O"),
            ASICLexer.DECIMAL: (10, "0D", "D"),
            ASICLexer.HEXADECIMAL: (16, "0X", "H"),
        }

        rule = rules.get(token.type)
        if not rule:
            raise AssemblerError(f"Unknown constant: {text}", self.source_line, ctx.start.column)

        base, prefix, suffix = rule
        t = text.upper()

        if t.startswith(prefix):
            t = t[2:]
        elif t.endswith(suffix):
            t = t[:-1]

        return int(t, base)

    def visit_if_not_null(self, expr):
        if expr is None:
            return None
        return self.visit(expr)
