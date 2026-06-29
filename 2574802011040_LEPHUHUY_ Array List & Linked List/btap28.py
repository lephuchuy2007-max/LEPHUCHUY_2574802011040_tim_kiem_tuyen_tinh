"""
Bài 13: Sắp xếp danh sách liên kết bằng merge sort
"""
from btap16 import SinglyLinkedList, Node

def split(head):
    slow=head; fast=head; prev=None
    while fast and fast.next:
        prev=slow; slow=slow.next; fast=fast.next.next
    if prev: prev.next=None
    return head, slow

def merge(l1,l2):
    dummy=Node(0); cur=dummy
    while l1 and l2:
        if l1.val<=l2.val: cur.next=l1; l1=l1.next
        else: cur.next=l2; l2=l2.next
        cur=cur.next
    cur.next = l1 or l2
    return dummy.next

def merge_sort(head):
    if not head or not head.next: return head
    left,right = split(head)
    return merge(merge_sort(left), merge_sort(right))

def sort_list(lst:SinglyLinkedList):
    lst.head = merge_sort(lst.head)
    # fix tail
    t=lst.head; prev=None
    while t: prev=t; t=t.next
    lst.tail = prev

if __name__=='__main__':
    l=SinglyLinkedList(); [l.pushBack(x) for x in [3,1,2]]
    sort_list(l); print(l)