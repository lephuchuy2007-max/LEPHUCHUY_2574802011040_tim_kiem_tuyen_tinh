"""
Bài 10: Xóa nút thứ k từ cuối (một lượt, hai con trỏ)
"""
from btap16 import SinglyLinkedList

def remove_kth_from_end(lst:SinglyLinkedList,k):
    dummy=type('D',(),{})()
    dummy.next=lst.head
    first=dummy; second=dummy
    for _ in range(k+1):
        if first.next is None and _<k:
            raise IndexError
        first = first.next
    while first:
        first=first.next; second=second.next
    # second.next is the node to remove
    to_remove=second.next
    second.next = to_remove.next
    if second.next is None:
        lst.tail = second
    lst.head = dummy.next
    return to_remove.val

if __name__ == '__main__':
    l=SinglyLinkedList(); [l.pushBack(x) for x in [1,2,3,4,5]]
    remove_kth_from_end(l,2)
    print(l)