from collections import deque


def round_robin(processes, quantum):
    q = deque((i, t) for i, t in enumerate(processes))
    time = 0
    completion = [0] * len(processes)
    while q:
        idx, rem = q.popleft()
        run = min(rem, quantum)
        time += run
        rem -= run
        if rem == 0:
            completion[idx] = time
        else:
            q.append((idx, rem))
    return completion


if __name__ == '__main__':
    processes = [5, 1, 3]
    quantum = 2
    print(round_robin(processes, quantum))
