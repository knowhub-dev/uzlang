# test.py

from uzlang import tokenize
from parser import parse, PrintNode, IfNode

code = """
agar raqam > 3
    yoz "Bu katta son"
"""

tokens = tokenize(code)
ast = parse(tokens)

for node in ast:
    if isinstance(node, IfNode):
        print(f"IF: {node.o‘zgaruvchi} {node.operator} {node.qiymat}")
        for sub in node.tanasi:
            print(f"  PRINT: {sub.matn}")
    elif isinstance(node, PrintNode):
        print(f"PRINT: {node.matn}")

