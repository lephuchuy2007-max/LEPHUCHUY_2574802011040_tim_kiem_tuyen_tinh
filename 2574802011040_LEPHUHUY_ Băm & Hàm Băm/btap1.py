"""
Bài 1. Cài đặt bảng băm bằng chaining
Cài đặt bảng băm với danh sách liên kết tại mỗi bucket (separate chaining)
hỗ trợ put, get, remove
"""

class HashTableChaining:
    """Bảng băm xử lý va chạm bằng chaining"""
    
    def __init__(self, size=10):
        """Khởi tạo bảng băm với size bucket"""
        self.size = size
        self.table = [[] for _ in range(size)]  # Mỗi bucket là danh sách
    
    def _hash(self, key):
        """Tính vị trí bucket cho key"""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Thêm hoặc cập nhật cặp (key, value)"""
        index = self._hash(key)
        # Kiểm tra xem key đã tồn tại chưa
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Nếu chưa tồn tại, thêm vào cuối bucket
        self.table[index].append((key, value))
    
    def get(self, key, default=None):
        """Lấy giá trị theo key, trả về default nếu không tìm thấy"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return default
    
    def remove(self, key):
        """Xóa cặp (key, value)"""
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
    
    def __repr__(self):
        return str(self.table)


if __name__ == "__main__":
    # Ví dụ sử dụng
    ht = HashTableChaining(5)
    
    # Thêm phần tử
    ht.put('a', 1)
    ht.put('b', 2)
    ht.put('c', 3)
    
    # Lấy giá trị
    print("get('a'):", ht.get('a'))  # Output: 1
    print("get('b'):", ht.get('b'))  # Output: 2
    
    # Cập nhật giá trị
    ht.put('a', 10)
    print("get('a') after update:", ht.get('a'))  # Output: 10
    
    # Xóa phần tử
    ht.remove('b')
    print("get('b') after remove:", ht.get('b', 'NOT_FOUND'))  # Output: NOT_FOUND
    
    # Lấy giá trị không tồn tại
    print("get('xyz'):", ht.get('xyz', 'NOT_FOUND'))  # Output: NOT_FOUND
