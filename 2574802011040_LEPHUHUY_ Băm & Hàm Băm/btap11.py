"""
Bài 11. Cài đặt HashSet
Cài đặt tập hợp băm với add, contains, remove
"""

class HashSet:
    """Tập hợp băm (không có phần tử trùng)"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def add(self, key):
        """Thêm phần tử vào tập hợp"""
        index = self._hash(key)
        
        # Kiểm tra xem key đã tồn tại chưa
        for k in self.table[index]:
            if k == key:
                return False  # Phần tử đã tồn tại
        
        self.table[index].append(key)
        return True  # Thêm thành công
    
    def contains(self, key):
        """Kiểm tra xem phần tử có trong tập hợp không"""
        index = self._hash(key)
        for k in self.table[index]:
            if k == key:
                return True
        return False
    
    def remove(self, key):
        """Xóa phần tử khỏi tập hợp"""
        index = self._hash(key)
        self.table[index] = [k for k in self.table[index] if k != key]
    
    def __repr__(self):
        elements = []
        for bucket in self.table:
            elements.extend(bucket)
        return str(set(elements))


if __name__ == "__main__":
    hs = HashSet(5)
    
    # Ví dụ 1: Thêm phần tử
    print("Thêm 1, 1, 2:")
    hs.add(1)
    print(f"  add(1): {hs}")
    hs.add(1)  # Thêm lại
    print(f"  add(1): {hs}")
    hs.add(2)
    print(f"  add(2): {hs}")
    
    # Ví dụ 2: Kiểm tra chứa
    print(f"\ncontains(1): {hs.contains(1)}")
    print(f"contains(3): {hs.contains(3)}")
    
    # Ví dụ 3: Xóa
    print(f"\nXóa 1:")
    hs.remove(1)
    print(f"contains(1): {hs.contains(1)}")
    print(f"Set: {hs}")
    
    # Ví dụ 4: Thêm nhiều phần tử
    print(f"\nThêm 3, 4, 5:")
    for i in [3, 4, 5]:
        hs.add(i)
    print(f"Set: {hs}")
