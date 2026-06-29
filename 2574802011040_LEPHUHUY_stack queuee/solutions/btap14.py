"""Bài 14: Stock Span
"""

def stock_span(prices):
    n = len(prices)
    res = [0]*n
    stack = []  # indices with decreasing prices
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        res[i] = i - (stack[-1] if stack else -1)
        stack.append(i)
    return res

if __name__ == '__main__':
    print(stock_span([100,80,60,70,60,75,85]))
