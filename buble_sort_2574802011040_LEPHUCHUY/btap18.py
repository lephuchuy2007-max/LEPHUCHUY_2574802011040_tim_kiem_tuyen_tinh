# btap18.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head:
        return None
    end = None
    while end != head.next:
        ptr = head
        while ptr.next != end:
            next_node = ptr.next
            if ptr.data > next_node.data:
                ptr.data, next_node.data = next_node.data, ptr.data
            ptr = ptr.next
        end = ptr
    return head

def print_list(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    res.append("null")
    print("-".join(res))

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head = bubble_sort_linked_list(head)
    print_list(head)