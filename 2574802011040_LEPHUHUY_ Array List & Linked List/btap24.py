"""
Bài 9: Trộn hai danh sách liên kết đã sắp xếp (nối lại các nút)
"""
from btap16 import SinglyLinkedList, Node

def merge_two_lists(l1:SinglyLinkedList, l2:SinglyLinkedList):
    dummy=Node(0); cur=dummy
    p=l1.head; q=l2.head
    while p and q:
        if p.val <= q.val:
            cur.next=p; p=p.next
        else:
            cur.next=q; q=q.next
        cur=cur.next
    cur.next = p or q
    res = SinglyLinkedList(); res.head=dummy.next
    # fix tail
    t=res.head
    prev=None
    while t: prev=t; t=t.next
    res.tail=prev
    return res

if __name__ == '__main__':
    a=SinglyLinkedList(); [a.pushBack(x) for x in [1,3,5]]
    b=SinglyLinkedList(); [b.pushBack(x) for x in [2,4]]
    print(merge_two_lists(a,b))