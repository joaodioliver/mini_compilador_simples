import re

TOKEN_PATTERNS = [
    ("NUM", r"\d+"),
    ("PLUS", r"\+"),
    ("PRINT", r"print"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("WS", r"\s+"),
]

def tokenize(source_code):
    pos = 0
    tokens = []
    while pos < len(source_code):
        match = None
        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            m = regex.match(source_code, pos)
            if m:
                text = m.group(0)
                if token_type != "WS":
                    tokens.append((token_type, text))
                pos = m.end()
                match = True
                break
        if not match:
            raise SyntaxError(f"Caractere inesperado: {source_code[pos]}")
    return tokens