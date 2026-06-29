"""
Bài 8: Phát hiện chu trình (Floyd)
"""
from btap16 import SinglyLinkedList

def has_cycle(lst:SinglyLinkedList):
    slow=fast=lst.head
    while fast and fast.next:
        slow=slow.next; fast=fast.next.next
        if slow==fast: return True
    return False

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushBack(1); l.pushBack(2); l.pushBack(3)
    print(has_cycle(l))