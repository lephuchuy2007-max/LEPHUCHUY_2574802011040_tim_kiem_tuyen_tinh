"""
Bài 2: Tính độ dài / duyệt
"""
from btap16 import SinglyLinkedList

def length(lst:SinglyLinkedList):
    cnt=0; cur=lst.head
    while cur:
        cnt+=1; cur=cur.next
    return cnt

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushBack(1); l.pushBack(2); l.pushBack(3)
    print(length(l))