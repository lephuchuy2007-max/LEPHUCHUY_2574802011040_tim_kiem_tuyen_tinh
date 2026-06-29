class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def remove_kth_from_end(head, k):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    for _ in range(k + 1):
        if first:
            first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next


def build_list(vals):
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print('->'.join(vals) + '->null')


if __name__ == '__main__':
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_kth_from_end(head, 2)
    print_list(new_head)
