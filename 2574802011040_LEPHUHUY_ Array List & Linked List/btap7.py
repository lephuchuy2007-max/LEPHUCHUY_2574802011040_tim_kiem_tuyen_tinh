"""
Bài 7: Phân tích amortized của append (giải thích ngắn trong comment)
"""
# Chứng minh: thao tác append phần lớn O(1); khi resize (gấp đôi) chi phí O(n),
# nhưng tổng chi phí cho n append là O(n) => amortized O(1).

def amortized_explanation():
    return ('n appends do at most O(n) copies when doubling; amortized O(1) each')

if __name__ == '__main__':
    print(amortized_explanation())