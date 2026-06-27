from typing import Never

from antlr4 import ParserRuleContext

from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError
from models.exceptions.AssemblerUndefinedError import AssemblerUndefinedError


def raise_syntax_error(msg: str, ctx: ParserRuleContext = None) -> Never:
    line = None
    column = None
    if ctx is not None:
        line = ctx.start.line
        column = ctx.start.column
    raise AssemblerSyntaxError(message=msg, line=line, column=column)


def raise_undefined_error(identifier: str, msg: str = None, ctx: ParserRuleContext = None) -> Never:
    line = None
    column = None
    if ctx is not None:
        line = ctx.start.line
        column = ctx.start.column
    raise AssemblerUndefinedError(identifier=identifier, message=msg, line=line, column=column)
