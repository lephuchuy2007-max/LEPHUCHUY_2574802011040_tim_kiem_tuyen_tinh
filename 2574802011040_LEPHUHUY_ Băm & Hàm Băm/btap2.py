"""
Bài 2. Cài đặt bảng băm bằng dò tuyến tính
Cài đặt bảng băm địa chỉ mở (open addressing) với linear probing
Khi va chạm tại idx i → thử i+1, i+2, ...
"""

class HashTableLinearProbing:
    """Bảng băm xử lý va chạm bằng linear probing"""
    
    def __init__(self, size=11):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.tombstone = object()  # Đánh dấu phần tử đã xóa
    
    def _hash(self, key):
        """Tính vị trí hash ban đầu"""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Thêm hoặc cập nhật cặp (key, value)"""
        index = self._hash(key)
        original_index = index
        
        # Dò tìm vị trí rỗng hoặc key tồn tại
        while self.keys[index] is not None and self.keys[index] is not self.tombstone:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
            if index == original_index:  # Tránh vòng lặp vô hạn
                raise Exception("Hash table is full")
        
        # Đặt key, value tại vị trí tìm được
        self.keys[index] = key
        self.values[index] = value
    
    def get(self, key, default=None):
        """Lấy giá trị theo key"""
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        
        return default
    
    def remove(self, key):
        """Xóa cặp (key, value) bằng lazy deletion"""
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = self.tombstone  # Đánh dấu xóa, không xóa hẳn
                self.values[index] = None
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        
        return False


if __name__ == "__main__":
    ht = HashTableLinearProbing(11)
    
    # Thêm phần tử
    ht.put('a', 1)
    ht.put('b', 2)
    ht.put('c', 3)
    
    print("get('a'):", ht.get('a'))  # Output: 1
    print("get('b'):", ht.get('b'))  # Output: 2
    
    # Cập nhật
    ht.put('a', 10)
    print("get('a') after update:", ht.get('a'))  # Output: 10
    
    # Xóa
    ht.remove('b')
    print("get('b') after remove:", ht.get('b', 'NOT_FOUND'))  # Output: NOT_FOUND
    
    print("get('c'):", ht.get('c'))  # Output: 3
