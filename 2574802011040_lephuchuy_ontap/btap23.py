def eval_rpn(expr):
    stack = []
    tokens = expr.split()
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[-1]


if __name__ == '__main__':
    print(eval_rpn('3 4 + 2 *'))
