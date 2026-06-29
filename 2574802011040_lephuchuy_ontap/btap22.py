class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


if __name__ == '__main__':
    ms = MinStack()
    ms.push(5)
    ms.push(3)
    ms.push(7)
    print(ms.get_min())
