from antlr4.error.ErrorListener import ErrorListener

from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError


class AssemblerErrorListener(ErrorListener):
    """Custom error listener that raises AssemblerError on syntax errors."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_info = {
            'line': line,
            'column': column,
            'message': msg,
            'offending_symbol': str(offendingSymbol) if offendingSymbol else None
        }
        self.errors.append(error_info)

        raise AssemblerSyntaxError(
            f"Syntax error: {msg}",
            line=line,
            column=column
        )

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass