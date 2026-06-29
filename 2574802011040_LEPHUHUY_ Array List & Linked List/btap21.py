"""
Bài 6: Đảo ngược danh sách liên kết (lặp và đệ quy)
"""
from btap16 import SinglyLinkedList, Node

def reverse_iterative(lst:SinglyLinkedList):
    prev=None; cur=lst.head
    while cur:
        nxt=cur.next; cur.next=prev; prev=cur; cur=nxt
    lst.head, lst.tail = prev, lst.head

def reverse_recursive_node(node):
    if node is None or node.next is None:
        return node
    new_head = reverse_recursive_node(node.next)
    node.next.next = node
    node.next = None
    return new_head

def reverse_recursive(lst:SinglyLinkedList):
    lst.tail = lst.head
    lst.head = reverse_recursive_node(lst.head)

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushBack(1); l.pushBack(2); l.pushBack(3)
    reverse_iterative(l); print(l)
    reverse_recursive(l); print(l)