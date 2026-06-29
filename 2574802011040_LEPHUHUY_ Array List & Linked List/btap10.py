"""
Bài 10: Trộn hai danh sách đã sắp xếp
"""
def merge_sorted(a, b):
    i=j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res

if __name__ == '__main__':
    print(merge_sorted([1,3,5],[2,4]))