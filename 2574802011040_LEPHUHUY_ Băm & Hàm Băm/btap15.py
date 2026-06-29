"""
Bài 15. Băm nhất quán (Consistent Hashing)
Thiết kế consistent hashing để phân tán khóa cho nhiều máy chủ
Khi thêm/bớt một máy chủ, số khóa phải di chuyển là tối thiểu
"""

import hashlib


class ConsistentHashing:
    """Consistent hashing với virtual nodes"""
    
    def __init__(self, replicas=3):
        """
        replicas: số nút ảo (virtual nodes) cho mỗi máy chủ
        """
        self.replicas = replicas
        self.ring = {}  # {position: server}
        self.sorted_positions = []
    
    def _hash(self, key):
        """Tính hash sử dụng MD5"""
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16)
    
    def add_server(self, server):
        """Thêm máy chủ vào ring"""
        print(f">>> Thêm server: {server}")
        for i in range(self.replicas):
            # Tạo nút ảo cho mỗi bản sao
            virtual_node = f"{server}:{i}"
            position = self._hash(virtual_node)
            self.ring[position] = server
        
        self.sorted_positions = sorted(self.ring.keys())
    
    def remove_server(self, server):
        """Xóa máy chủ khỏi ring"""
        print(f">>> Xóa server: {server}")
        positions_to_remove = []
        for position, srv in self.ring.items():
            if srv == server:
                positions_to_remove.append(position)
        
        for position in positions_to_remove:
            del self.ring[position]
        
        self.sorted_positions = sorted(self.ring.keys())
    
    def get_server(self, key):
        """Tìm máy chủ phục vụ key"""
        if not self.sorted_positions:
            return None
        
        position = self._hash(key)
        
        # Tìm máy chủ có position >= key position
        for node_pos in self.sorted_positions:
            if node_pos >= position:
                return self.ring[node_pos]
        
        # Quay về đầu ring
        return self.ring[self.sorted_positions[0]]
    
    def get_distribution(self, keys):
        """Phân bố các khóa đến các máy chủ"""
        distribution = {}
        for key in keys:
            server = self.get_server(key)
            distribution[server] = distribution.get(server, 0) + 1
        return distribution


if __name__ == "__main__":
    ch = ConsistentHashing(replicas=3)
    
    print("=== THÊM 3 MÁYĐỤ ===")
    ch.add_server('server1')
    ch.add_server('server2')
    ch.add_server('server3')
    
    # Phân bố khóa
    keys = [f'user:{i}' for i in range(100)]
    distribution1 = ch.get_distribution(keys)
    print(f"\nPhân bố ban đầu: {distribution1}")
    
    print("\n=== THÊM server4 ===")
    ch.add_server('server4')
    distribution2 = ch.get_distribution(keys)
    print(f"Phân bố sau khi thêm: {distribution2}")
    
    # Tính số khóa di chuyển
    moved = 0
    for server in distribution1:
        if server in distribution2:
            moved += abs(distribution1[server] - distribution2[server])
    print(f"Ước lượng khóa di chuyển: ~{moved // 2}")
    
    print("\n--- PHÂN TÍCH ---")
    print("Consistent Hashing:")
    print("  + Khi thêm/bớt server, chỉ ~1/n khóa cần di chuyển")
    print("  + Hoạt động tốt cho distributed cache/database")
    print("  + Có thể tùy chỉnh replication factor")
    print("\nNhược điểm:")
    print("  - Phức tạp hơn simple hash modulo")
    print("  - Cần quản lý virtual nodes")
