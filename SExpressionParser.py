import re

class SExpressionParser:
    def __init__(self):
        self.expression = None
        self.index = 0

    def parse(self, expression):
        self.expression = expression.replace('(', ' ( ').replace(')', ' ) ')
        self.index = 0
        tokens = self.tokenize()

        return self.parse_tokens(tokens)

    def parse_tokens(self, tokens):
        if not tokens:
            return None

        current_token = tokens.pop(0)

        if current_token == '(':
            sub_expr = []
            while tokens[0] != ')':
                sub_expr.append(self.parse_tokens(tokens))
            tokens.pop(0)  # Remove ')'
            return sub_expr
        elif current_token.isdigit() or (current_token[0] == '-' and current_token[1:].isdigit()):
            return int(current_token)
        elif re.match(r'^[+\-*/]$', current_token):
            return current_token
        else:
            raise ValueError(f"Unexpected token: {current_token}")

    def tokenize(self):
        return self.expression.split()

# Example usage:
sexpression_parser = SExpressionParser()
result = sexpression_parser.parse("(+ 3 (* 4 5))")
print(result)
