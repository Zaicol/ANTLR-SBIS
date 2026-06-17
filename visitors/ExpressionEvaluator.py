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
        return super().visit(ctx)

    def visitExpression(self, ctx: ASICParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitAdditive_expression(self, ctx: ASICParser.Additive_expressionContext):
        left = self.visit(ctx.multiplicative_expression(0))
        right = self.visit(ctx.multiplicative_expression(1))
        if ctx.addop(0).getText() != '+':
            raise AssemblerSyntaxError("Unknown operator: " + ctx.addop(0).getText(), self.line)
        return left + right

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

        if not (0 <= value <= 255):
            raise BitValueError(f"Константа {text} не помещается в 8 бит (допустимый диапазон: 0–255)")

        return value
