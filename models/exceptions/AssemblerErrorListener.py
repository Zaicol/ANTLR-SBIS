from antlr4.error.ErrorListener import ErrorListener

from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError


class AssemblerErrorListener(ErrorListener):
    """Custom error listener that raises AssemblerError on syntax errors."""

    def __init__(self):
        super().__init__()
        self.errors = {
            "syntax": [],
            "ambiguity": [],
            "attempting_full_context": [],
            "context_sensitivity": []
        }

    def raise_errors(self):
        if not self.has_errors():
            return

        syntax_errors = self.errors["syntax"]
        error_message = "Found the following syntax errors:\n"
        for error in syntax_errors:
            error_message += f"Line {error['line']}, Column {error['column']}: {error['message']}\n"
        raise AssemblerSyntaxError(error_message)

    def has_errors(self):
        return len(self.errors["syntax"]) > 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_info = {
            'type': 'syntax',
            'line': line,
            'column': column,
            'message': msg,
            'offending_symbol': str(offendingSymbol) if offendingSymbol else None
        }
        self.errors["syntax"].append(error_info)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        error_info = {
            'type': 'ambiguity',
            'start_index': startIndex,
            'stop_index': stopIndex,
            'exact': exact,
            'ambiguous_alternatives': list(ambigAlts) if ambigAlts else None,
            'configs_size': len(configs) if configs else 0
        }
        self.errors["ambiguity"].append(error_info)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        error_info = {
            'type': 'attempting_full_context',
            'start_index': startIndex,
            'stop_index': stopIndex,
            'conflicting_alternatives': list(conflictingAlts) if conflictingAlts else None,
            'configs_size': len(configs) if configs else 0
        }
        self.errors["attempting_full_context"].append(error_info)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        error_info = {
            'type': 'context_sensitivity',
            'start_index': startIndex,
            'stop_index': stopIndex,
            'prediction': prediction,
            'configs_size': len(configs) if configs else 0
        }
        self.errors["context_sensitivity"].append(error_info)