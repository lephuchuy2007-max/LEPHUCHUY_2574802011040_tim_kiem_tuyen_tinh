class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None


def build_list(vals, pos=-1):
    dummy = ListNode()
    tail = dummy
    cycle_node = None
    for i, v in enumerate(vals):
        tail.next = ListNode(v)
        tail = tail.next
        if i == pos:
            cycle_node = tail
    if pos != -1:
        tail.next = cycle_node
    return dummy.next


def print_node(node):
    if node:
        print(node.val)
    else:
        print(None)


if __name__ == '__main__':
    head = build_list([3, 2, 0, -4], pos=1)
    print_node(detect_cycle(head))
