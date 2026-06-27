from bisect import bisect_left
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


def split_cycles_generator(remaining_cycles: int):
    while remaining_cycles > 255:
        yield 255
        remaining_cycles -= 255
    if remaining_cycles > 0:
        yield remaining_cycles


def get_closest_line(source_line_map: dict[int, int], source_line: int) -> int:
    if source_line in source_line_map:
        return source_line_map[source_line]

    keys = sorted(source_line_map.keys())
    i = bisect_left(keys, source_line)

    closest_next_line = keys[i] if i < len(keys) else None

    if closest_next_line is None:
        raise_syntax_error(f"Can't find closest instruction for source line: {source_line}", None)

    return source_line_map[closest_next_line]
