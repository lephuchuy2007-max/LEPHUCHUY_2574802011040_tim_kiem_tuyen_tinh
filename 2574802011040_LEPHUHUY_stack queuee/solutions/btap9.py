"""Bài 9: Chuyển trung tố sang hậu tố (shunting-yard)
"""

def infix_to_postfix(expr: str) -> str:
    prec = {'+':1, '-':1, '*':2, '/':2}
    output = []
    ops = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isalnum():
            output.append(c)
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()
        elif c in prec:
            while ops and ops[-1] != '(' and prec.get(ops[-1],0) >= prec[c]:
                output.append(ops.pop())
            ops.append(c)
        i += 1
    while ops:
        output.append(ops.pop())
    return ' '.join(output)

if __name__ == '__main__':
    print(infix_to_postfix('a+b*c'))  # a b c * +
