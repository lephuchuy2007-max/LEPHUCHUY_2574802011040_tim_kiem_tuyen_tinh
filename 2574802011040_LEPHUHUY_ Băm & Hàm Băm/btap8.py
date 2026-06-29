"""
Bài 8. Quadratic probing / double hashing
Cài đặt quadratic probing và double hashing để giảm gom cụm (clustering)
"""

class QuadraticProbingHashTable:
    """Xử lý va chạm bằng quadratic probing"""
    
    def __init__(self, size=11):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        step = 0
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            step += 1
            # Quadratic probing: thử i+1², i+2², i+3², ...
            index = (self._hash(key) + step * step) % self.size
        
        self.keys[index] = key
        self.values[index] = value
    
    def get(self, key, default=None):
        index = self._hash(key)
        step = 0
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            step += 1
            index = (self._hash(key) + step * step) % self.size
        
        return default


class DoubleHashingHashTable:
    """Xử lý va chạm bằng double hashing"""
    
    def __init__(self, size=11):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
    
    def _hash1(self, key):
        """Hàm hash chính"""
        return hash(key) % self.size
    
    def _hash2(self, key):
        """Hàm hash thứ hai - phải nguyên tố cùng size"""
        return 1 + (hash(key) % (self.size - 1))
    
    def put(self, key, value):
        index = self._hash1(key)
        step = 0
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            step += 1
            # Double hashing: thử i + 1*h2(k), i + 2*h2(k), ...
            index = (self._hash1(key) + step * self._hash2(key)) % self.size
        
        self.keys[index] = key
        self.values[index] = value
    
    def get(self, key, default=None):
        index = self._hash1(key)
        step = 0
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            step += 1
            index = (self._hash1(key) + step * self._hash2(key)) % self.size
        
        return default


if __name__ == "__main__":
    print("=== QUADRATIC PROBING ===")
    q = QuadraticProbingHashTable(11)
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for k in keys:
        q.put(k, k)
    print("Keys:", q.keys)
    
    print("\n=== DOUBLE HASHING ===")
    d = DoubleHashingHashTable(11)
    for k in keys:
        d.put(k, k)
    print("Keys:", d.keys)
    
    print("\n--- KẾT LUẬN ---")
    print("Quadratic Probing:")
    print("  + Giảm primary clustering")
    print("  - Có thể xảy ra secondary clustering")
    
    print("\nDouble Hashing:")
    print("  + Giảm tất cả loại clustering")
    print("  + Phân bố tốt hơn khi load factor cao")
    print("  - Phức tạp hơn, cần hai hàm hash")
