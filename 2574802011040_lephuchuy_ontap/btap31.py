class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = x
        self.size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError('Index out of range')
        return self.data[idx]

    def __len__(self):
        return self.size


if __name__ == '__main__':
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print(len(arr), arr.capacity)
