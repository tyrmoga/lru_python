 #Each node has a key and value, as well as pointers to the next and previous nodes in the linked list.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

#Next, we define the cache structure

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} #this is the hashmap that will store the key-value pairs for O(1) access time
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        #we are using two dummy nodes, head and tail, to simplify the insertion and deletion of nodes in the linked list. The head node will always point to the most recently used node, while the tail node will always point to the least recently used node.
#
#Next, we define the helper methods for the LRUCache class
    def _remove(self, node):
        #removes a node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        #inserts a node into the linked list
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        