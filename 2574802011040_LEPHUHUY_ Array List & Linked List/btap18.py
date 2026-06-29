"""
Bài 3: Tìm kiếm một giá trị (return index or -1)
"""
from btap16 import SinglyLinkedList

def find_index(lst:SinglyLinkedList, x):
    idx=0; cur=lst.head
    while cur:
        if cur.val==x: return idx
        idx+=1; cur=cur.next
    return -1

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushBack(1); l.pushBack(2); l.pushBack(3)
    print(find_index(l,2))