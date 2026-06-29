"""Bài 15: Lập lịch xoay vòng (Round-Robin) - simple simulator
"""

def round_robin(processes, quantum):
    # processes: list of (pid, burst_time)
    from collections import deque
    q = deque([(pid, bt) for pid, bt in processes])
    time = 0
    completion = {}
    while q:
        pid, bt = q.popleft()
        run = min(bt, quantum)
        time += run
        bt -= run
        if bt > 0:
            q.append((pid, bt))
        else:
            completion[pid] = time
    return completion

if __name__ == '__main__':
    print(round_robin([(1,5),(2,3),(3,8)], 2))
