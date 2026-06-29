"""
Bài 7: Tìm nút giữa (slow/fast)
"""
from btap16 import SinglyLinkedList

def find_middle(lst:SinglyLinkedList):
    slow=fast=lst.head
    while fast and fast.next:
        slow=slow.next; fast=fast.next.next
    return slow

if __name__ == '__main__':
    l=SinglyLinkedList(); [l.pushBack(x) for x in [1,2,3,4,5]]
    print(find_middle(l).val)