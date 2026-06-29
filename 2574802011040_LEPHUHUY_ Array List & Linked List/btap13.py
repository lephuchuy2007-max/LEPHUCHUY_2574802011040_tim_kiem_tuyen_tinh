"""
Bài 13: Merge Intervals
"""
def merge_intervals(intervals):
    if not intervals: return []
    intervals = sorted(intervals, key=lambda x: x[0])
    res=[intervals[0]]
    for s,e in intervals[1:]:
        last_s,last_e = res[-1]
        if s <= last_e:
            res[-1][1] = max(last_e,e)
        else:
            res.append([s,e])
    return res

if __name__ == '__main__':
    print(merge_intervals([[1,3],[2,6],[8,10]]))