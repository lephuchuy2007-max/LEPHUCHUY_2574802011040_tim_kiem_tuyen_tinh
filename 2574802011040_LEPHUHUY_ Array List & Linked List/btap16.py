"""
PHẦN B — LINKED LIST
Bài 1: Singly linked list (pushFront, pushBack, print)
"""
class Node:
    def __init__(self,val,next=None):
        self.val=val; self.next=next

class SinglyLinkedList:
    def __init__(self):
        self.head=None; self.tail=None

    def pushFront(self,val):
        node=Node(val,self.head)
        self.head=node
        if self.tail is None: self.tail=node

    def pushBack(self,val):
        node=Node(val)
        if not self.head:
            self.head=self.tail=node
        else:
            self.tail.next=node; self.tail=node

    def __repr__(self):
        res=[]
        cur=self.head
        while cur:
            res.append(str(cur.val)); cur=cur.next
        return '->'.join(res)+'->null'

if __name__ == '__main__':
    l=SinglyLinkedList(); l.pushFront(2); l.pushBack(5); print(l)