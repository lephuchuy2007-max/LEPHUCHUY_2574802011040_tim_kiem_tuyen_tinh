"""Bài 8: Tính biểu thức hậu tố (RPN)
"""

def evaluate_postfix(expr: str):
    tokens = expr.split()
    st = []
    for t in tokens:
        if t.lstrip('-').isdigit():
            st.append(int(t))
        else:
            b = st.pop(); a = st.pop()
            if t == '+': st.append(a+b)
            elif t == '-': st.append(a-b)
            elif t == '*': st.append(a*b)
            elif t == '/': st.append(int(a/b))
            else: raise ValueError('op')
    return st[-1]

if __name__ == '__main__':
    print(evaluate_postfix('3 4 + 2 *'))  # 14
