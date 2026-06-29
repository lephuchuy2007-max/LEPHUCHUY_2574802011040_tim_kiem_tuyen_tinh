"""
Bài 14: Cộng hai số biểu diễn bằng linked list
"""
from btap16 import SinglyLinkedList

def add_two_numbers(l1:SinglyLinkedList, l2:SinglyLinkedList):
    p=l1.head; q=l2.head; carry=0
    res=SinglyLinkedList()
    while p or q or carry:
        s = carry + (p.val if p else 0) + (q.val if q else 0)
        res.pushBack(s%10); carry = s//10
        p = p.next if p else None
        q = q.next if q else None
    return res

if __name__=='__main__':
    a=SinglyLinkedList(); [a.pushBack(x) for x in [2,4,3]]
    b=SinglyLinkedList(); [b.pushBack(x) for x in [5,6,4]]
    print(add_two_numbers(a,b))