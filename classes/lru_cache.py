from doubly_linked_list import Node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next

        prev.nxt = nxt
        nxt.prev = prev
    
    def _move_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key:int) -> int | None:
        if key not in self.map:
            return None
        
        node = self.map[key]
        self._remove(node)
        self._move_to_head(node)

        return node.value
    
    def put(self, key: int, value: int):
        if key in self.map:
            node = self.map[key]
            node.value = value
            
            self._remove(node)
            self._move_to_head(node)
            return

        if len(self.map) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        new_node = Node(key, value)
        self.map[key] = new_node
        self._move_to_head(new_node)