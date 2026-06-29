"""
Bài 12: Tìm điểm bắt đầu chu trình (Floyd phase 2)
"""
from btap23 import has_cycle
from btap16 import SinglyLinkedList

def find_cycle_start(lst:SinglyLinkedList):
    slow=fast=lst.head
    while fast and fast.next:
        slow=slow.next; fast=fast.next.next
        if slow==fast:
            break
    else:
        return None
    slow = lst.head
    while slow!=fast:
        slow=slow.next; fast=fast.next
    return slow

if __name__=='__main__':
    l=SinglyLinkedList(); [l.pushBack(x) for x in [1,2,3,4]]
    # make a cycle for demo
    l.tail.next = l.head.next
    print(find_cycle_start(l).val)