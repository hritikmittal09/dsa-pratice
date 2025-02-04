class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        
        """
        :type capacity: int
        """
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev   

    def _insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key):

        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)  # Move to end (recently used)
        self._insert(node)
        return node.value
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])  # Remove old node
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)  # Insert as most recently used

        if len(self.cache) > self.capacity:
            # Remove least recently used (LRU)
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]


        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)