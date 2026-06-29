"""
Bài 11: Doubly linked list (basic)
"""
class DNode:
    def __init__(self,val,prev=None,next=None):
        self.val=val; self.prev=prev; self.next=next

class DoublyLinkedList:
    def __init__(self):
        self.head=None; self.tail=None

    def pushFront(self,val):
        node=DNode(val,None,self.head)
        if self.head: self.head.prev=node
        self.head=node
        if self.tail is None: self.tail=node

    def pushBack(self,val):
        node=DNode(val,self.tail,None)
        if self.tail: self.tail.next=node
        self.tail=node
        if self.head is None: self.head=node

    def __repr__(self):
        res=[]; cur=self.head
        while cur: res.append(str(cur.val)); cur=cur.next
        return '<->'.join(res)

if __name__=='__main__':
    d=DoublyLinkedList(); d.pushFront(1); d.pushBack(2); print(d)