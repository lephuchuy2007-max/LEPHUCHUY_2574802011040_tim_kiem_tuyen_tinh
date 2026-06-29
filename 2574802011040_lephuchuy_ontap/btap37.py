class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def build_list(vals):
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def print_node(node):
    if node:
        print(node.val)
    else:
        print(None)


if __name__ == '__main__':
    head = build_list([1, 2, 3, 4, 5])
    print_node(middle_node(head))
