"""
Bài 30. MinHash ước lượng độ tương đồng
Dùng MinHash (nhiều hàm băm) để ước lượng độ tương đồng Jaccard
giữa hai tập hợp lớn mà không cần so sánh trực tiếp toàn bộ
"""

import random


class MinHashSketch:
    """MinHash Sketch cho ước lượng độ tương đồng Jaccard"""
    
    def __init__(self, num_hashes=100):
        """
        num_hashes: số hàm băm (sketch size)
        """
        self.num_hashes = num_hashes
        self.hash_funcs = []
        
        # Tạo các hàm băm ngẫu nhiên
        random.seed(42)
        for _ in range(num_hashes):
            a = random.randint(1, 10**9)
            b = random.randint(1, 10**9)
            self.hash_funcs.append((a, b))
    
    def compute_hash(self, value, a, b):
        """Tính hash cho một giá trị với hàm (a, b)"""
        return (a * value + b) % (10**9 + 7)
    
    def compute_sketch(self, s):
        """Tính MinHash sketch cho tập hợp s"""
        sketch = []
        
        for a, b in self.hash_funcs:
            # Tìm giá trị min hash trong tập
            min_hash = float('inf')
            for item in s:
                h = self.compute_hash(hash(item), a, b)
                min_hash = min(min_hash, h)
            
            sketch.append(min_hash)
        
        return sketch
    
    def estimate_jaccard(self, sketch1, sketch2):
        """Ước lượng độ tương đồng Jaccard từ 2 sketches"""
        matches = sum(1 for h1, h2 in zip(sketch1, sketch2) if h1 == h2)
        return matches / self.num_hashes


def jaccard_similarity(s1, s2):
    """Tính độ tương đồng Jaccard thật"""
    if not s1 and not s2:
        return 1.0
    intersection = len(s1 & s2)
    union = len(s1 | s2)
    return intersection / union if union > 0 else 0


if __name__ == "__main__":
    print("=== MINHASH ===\n")
    
    # Ví dụ 1
    print("Ví dụ 1: Ước lượng Jaccard similarity")
    print("-" * 50)
    
    s1 = {1, 2, 3, 4, 5}
    s2 = {3, 4, 5, 6, 7}
    
    mh = MinHashSketch(num_hashes=100)
    
    # Tính Jaccard thật
    true_jaccard = jaccard_similarity(s1, s2)
    print(f"Tập 1: {s1}")
    print(f"Tập 2: {s2}")
    print(f"Jaccard thật: {true_jaccard:.4f}")
    
    # Ước lượng bằng MinHash
    sketch1 = mh.compute_sketch(s1)
    sketch2 = mh.compute_sketch(s2)
    estimated_jaccard = mh.estimate_jaccard(sketch1, sketch2)
    print(f"MinHash ước lượng: {estimated_jaccard:.4f}")
    print(f"Sai số: {abs(true_jaccard - estimated_jaccard):.4f}")
    
    # Ví dụ 2: Nhiều tập khác nhau
    print("\n" + "=" * 50)
    print("Ví dụ 2: So sánh nhiều cặp")
    print("-" * 50)
    
    sets = [
        {1, 2, 3, 4, 5},
        {3, 4, 5, 6, 7},
        {1, 2, 3},
        {5, 6, 7, 8, 9}
    ]
    
    # Tính tất cả sketches
    sketches = [mh.compute_sketch(s) for s in sets]
    
    print(f"{'Pair':<12} {'True':<10} {'MinHash':<10} {'Error':<10}")
    print("-" * 42)
    
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            true_sim = jaccard_similarity(sets[i], sets[j])
            est_sim = mh.estimate_jaccard(sketches[i], sketches[j])
            error = abs(true_sim - est_sim)
            print(f"({i},{j})       {true_sim:.4f}     {est_sim:.4f}     {error:.4f}")
    
    # Ví dụ 3: Ảnh hưởng của số hashes
    print("\n" + "=" * 50)
    print("Ví dụ 3: Ảnh hưởng của num_hashes")
    print("-" * 50)
    
    s1_large = set(range(100, 200))
    s2_large = set(range(150, 250))
    
    true_large = jaccard_similarity(s1_large, s2_large)
    print(f"True Jaccard: {true_large:.4f}")
    
    print(f"{'Num Hashes':<12} {'Estimate':<10} {'Error':<10}")
    for num_hashes in [10, 50, 100, 500, 1000]:
        mh_temp = MinHashSketch(num_hashes)
        sk1 = mh_temp.compute_sketch(s1_large)
        sk2 = mh_temp.compute_sketch(s2_large)
        est = mh_temp.estimate_jaccard(sk1, sk2)
        print(f"{num_hashes:<12} {est:.4f}     {abs(est - true_large):.4f}")
    
    print("\n--- PHÂN TÍCH ---")
    print("MinHash:")
    print("  ✓ Ước lượng Jaccard mà không cần lưu toàn bộ tập")
    print("  ✓ Bộ nhớ O(k) với k = số hashes")
    print("  ✓ So sánh 2 tập chỉ cần O(k)")
    print("  ✗ Độ chính xác tùy thuộc k")
    print("\nCông thức:")
    print("  P(hash1==hash2) = Jaccard(s1, s2)")
    print("  Estimate = (# matches) / k")
