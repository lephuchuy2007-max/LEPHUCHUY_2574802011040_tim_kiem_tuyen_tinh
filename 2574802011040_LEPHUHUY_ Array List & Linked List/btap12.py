"""
Bài 12: Loại bỏ trùng lặp giữ thứ tự
"""
def dedupe_n2(arr):
    res=[]
    for x in arr:
        found=False
        for y in res:
            if x==y:
                found=True; break
        if not found: res.append(x)
    return res

def dedupe_hash(arr):
    seen=set(); res=[]
    for x in arr:
        if x not in seen:
            seen.add(x); res.append(x)
    return res

if __name__ == '__main__':
    print(dedupe_hash([3,1,3,2,1]))