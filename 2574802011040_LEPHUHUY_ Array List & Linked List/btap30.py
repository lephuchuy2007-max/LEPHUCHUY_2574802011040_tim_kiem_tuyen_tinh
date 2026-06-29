"""
Bài 15: LRU Cache (doubly linked list + hashmap)
"""
class LRUNode:
    def __init__(self,k,v):
        self.k=k; self.v=v; self.prev=None; self.next=None

class LRUCache:
    def __init__(self,capacity):
        self.cap=capacity; self.map={}
        self.head=LRUNode(0,0); self.tail=LRUNode(0,0)
        self.head.next=self.tail; self.tail.prev=self.head

    def _remove(self,node):
        p=node.prev; n=node.next; p.next=n; n.prev=p

    def _add_front(self,node):
        node.next = self.head.next; node.prev = self.head
        self.head.next.prev = node; self.head.next = node

    def get(self,k):
        node=self.map.get(k)
        if not node: return -1
        self._remove(node); self._add_front(node)
        return node.v

    def put(self,k,v):
        if k in self.map:
            node=self.map[k]; node.v=v; self._remove(node); self._add_front(node)
        else:
            node=LRUNode(k,v); self.map[k]=node; self._add_front(node)
            if len(self.map)>self.cap:
                # remove last
                tail_prev=self.tail.prev
                self._remove(tail_prev); del self.map[tail_prev.k]

if __name__=='__main__':
    c=LRUCache(2); c.put(1,1); c.put(2,2); print(c.get(1)); c.put(3,3); print(c.get(2))