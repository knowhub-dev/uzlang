# testint.py

from uzlang import tokenize
from parser import parse, PrintNode, IfNode
from interpreter import Interpreter

code = """
agar raqam > 3
    yoz "Bu katta son"
"""

tokens = tokenize(code)
ast = parse(tokens)

interpreter = Interpreter()
interpreter.context['raqam'] = 5
interpreter.execute(ast[0])

