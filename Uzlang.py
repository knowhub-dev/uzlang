# uzlang.py

import re

def tokenize(code):
    tokens = []
    kod = code.strip().split('\n')
    for line in kod:
        line = line.strip()
        if not line:
            continue
        if line.startswith('agar'):
            tokens.append(('AGAR', 'agar'))
            qism = line[4:].strip()
            match = re.match(r'(\w+)\s*(==|!=|>=|<=|>|<)\s*(\w+)', qism)
            if match:
                tokens.append(('IDENTIFIKATOR', match.group(1)))
                tokens.append(('OPERATOR', match.group(2)))
                tokens.append(('QIYMAT', match.group(3)))
            tokens.append(('YANGI_QATOR', '\n'))
        elif line.startswith('yoz'):
            tokens.append(('YOZ', 'yoz'))
            matn = line[3:].strip()
            tokens.append(('MATN', matn))
    return tokens

