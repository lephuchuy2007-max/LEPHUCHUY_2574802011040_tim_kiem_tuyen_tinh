"""
Bài 5: Xóa nút theo giá trị (xóa nút đầu tiên có giá trị bằng x)
"""
from btap16 import SinglyLinkedList

def remove_value(lst:SinglyLinkedList, x):
    cur=lst.head; prev=None
    while cur:
        if cur.val==x:
            if prev is None:
                lst.head=cur.next
            else:
                prev.next=cur.next
            if cur.next is None:
                lst.tail=prev
            return True
        prev=cur; cur=cur.next
    return False

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushBack(1); l.pushBack(2); l.pushBack(3); l.pushBack(2)
    remove_value(l,2)
    print(l)