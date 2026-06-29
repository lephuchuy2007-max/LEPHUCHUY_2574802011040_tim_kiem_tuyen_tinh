class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def reverse_list_iterative(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_list_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


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
    head = build_list([1, 2, 3])
    print_list(reverse_list_iterative(head))
    head = build_list([1, 2, 3])
    print_list(reverse_list_recursive(head))
