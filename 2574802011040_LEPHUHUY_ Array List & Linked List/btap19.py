"""
Bài 4: Chèn sau một nút cho trước (ở đây theo vị trí k)
"""
from btap16 import SinglyLinkedList, Node

def insert_after(lst:SinglyLinkedList, k, val):
    cur=lst.head; idx=0
    if k<0: raise IndexError
    while cur and idx<k:
        cur=cur.next; idx+=1
    if cur is None:
        raise IndexError('position out of range')
    node=Node(val,cur.next)
    cur.next=node
    if node.next is None:
        lst.tail=node

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushBack(1); l.pushBack(3)
    insert_after(l,0,2)
    print(l)