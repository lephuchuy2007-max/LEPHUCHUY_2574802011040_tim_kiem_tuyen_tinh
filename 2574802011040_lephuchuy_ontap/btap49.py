import random


class UniversalHash:
    def __init__(self, m, p=10**9+7):
        self.m = m
        self.p = p
        self.a = random.randrange(1, p)
        self.b = random.randrange(0, p)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


if __name__ == '__main__':
    uh = UniversalHash(10)
    print(uh.hash(15))
