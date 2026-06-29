"""Bài 6: Dấu ngoặc cân bằng
Kiểm tra () [] {}
"""

def balanced_parentheses(s: str) -> bool:
    pairs = {')':'(', ']':'[', '}':'{'}
    st = []
    for ch in s:
        if ch in '([{':
            st.append(ch)
        elif ch in pairs:
            if not st or st[-1] != pairs[ch]:
                return False
            st.pop()
    return len(st) == 0

if __name__ == '__main__':
    print(balanced_parentheses('([]{})'))  # True
    print(balanced_parentheses('([)]'))    # False
