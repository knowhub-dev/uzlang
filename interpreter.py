# interpreter.py

class Interpreter:
    def __init__(self):
        self.context = {}

    def execute(self, node):
        if isinstance(node, PrintNode):
            print(eval(node.matn, {}, self.context))
        elif isinstance(node, IfNode):
            left = self.context.get(node.o‘zgaruvchi, 0)
            right = int(node.qiymat)
            op = node.operator
            if self.evaluate_condition(left, op, right):
                for sub_node in node.tanasi:
                    self.execute(sub_node)

    def evaluate_condition(self, left, operator, right):
        return {
            '==': left == right,
            '!=': left != right,
            '>': left > right,
            '<': left < right,
            '>=': left >= right,
            '<=': left <= right
        }[operator]

