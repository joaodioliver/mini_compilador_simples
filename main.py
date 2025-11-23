from meu_compilador.scanner import tokenize
from meu_compilador.syntax import build_ast
from meu_compilador.generator import generate_code

source = "print(2+3)"
tokens = tokenize(source)
ast = build_ast(tokens)
py_code = generate_code(ast)

print("Código gerado:")
print(py_code)
exec(py_code)