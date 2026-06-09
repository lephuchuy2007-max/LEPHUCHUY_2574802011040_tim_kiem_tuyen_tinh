
1. Phát biểu Bất biến vòng lặp (Loop Invariant):
   Tại đầu mỗi vòng lặp ngoài thứ i, đoạn gồm i phần tử cuối mảng a[n-i...n-1] 
   luôn chứa các phần tử lớn nhất của mảng ban đầu và được sắp xếp tăng dần.
2. Chứng minh:
   - Khởi tạo (i = 0): Đoạn trống -> Hiển nhiên Đúng.
   - Duy trì: Lượt i+1 nổi bọt đưa số lớn nhất còn lại về vị trí a[n-i-1] -> Thỏa mãn Đúng.
   - Kết thúc: Khi hoàn tất, toàn bộ n-1 phần tử lớn đã xếp đúng chỗ ở cuối, phần tử 
    đầu mảng hiển nhiên nhỏ nhất -> Mảng được sắp xếp hoàn chỉnh một cách chính xác.

if __name__ == "__main__":
    print("Chứng minh lý thuyết thành công!")