# parser.py

class IfNode:
    def __init__(self, o‘zgaruvchi, operator, qiymat, tanasi):
        self.o‘zgaruvchi = o‘zgaruvchi
        self.operator = operator
        self.qiymat = qiymat
        self.tanasi = tanasi

class PrintNode:
    def __init__(self, matn):
        self.matn = matn

def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'AGAR':
            o‘zgaruvchi = tokens[i+1][1]
            operator = tokens[i+2][1]
            qiymat = tokens[i+3][1]
            i += 5  # YANGI_QATOR
            tanasi = []
            if tokens[i][0] == 'YOZ':
                matn = tokens[i+1][1]
                tanasi.append(PrintNode(matn))
                i += 2
            ast.append(IfNode(o‘zgaruvchi, operator, qiymat, tanasi))
        elif token[0] == 'YOZ':
            matn = tokens[i+1][1]
            ast.append(PrintNode(matn))
            i += 2
        else:
            i += 1
    return ast

