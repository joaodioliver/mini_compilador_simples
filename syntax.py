def build_ast(tokens):
    if not tokens or tokens[0][0] != "PRINT":
        raise SyntaxError("Esperado 'print'")
    if len(tokens) < 3 or tokens[1][0] != "LPAREN" or tokens[-1][0] != "RPAREN":
        raise SyntaxError("Parênteses ausentes")
    expr = parse_expression(tokens[2:-1])
    return ("PRINT", expr)

def parse_expression(tokens):
    if len(tokens) == 1 and tokens[0][0] == "NUM":
        return ("NUM", tokens[0][1])
    if len(tokens) == 3 and tokens[0][0] == "NUM" and tokens[1][0] == "PLUS" and tokens[2][0] == "NUM":
        return ("ADD", tokens[0][1], tokens[2][1])
    raise SyntaxError("Expressão inválida")