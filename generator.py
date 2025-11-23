def generate_code(ast):
    kind = ast[0]
    if kind == "PRINT":
        return f"print({generate_code(ast[1])})"
    if kind == "ADD":
        return f"{ast[1]} + {ast[2]}"
    if kind == "NUM":
        return ast[1]
    raise ValueError(f"Nó desconhecido: {kind}")