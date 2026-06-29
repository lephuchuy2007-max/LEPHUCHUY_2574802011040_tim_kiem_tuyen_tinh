class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
n        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    return merge_two_lists(left, right)


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
    head = build_list([3, 1, 2])
    print_list(sort_list(head))
