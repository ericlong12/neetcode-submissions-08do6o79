class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # this will make key to node


        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        # we put it inside the list. on the rightmost position
        # because it is the most recently used
        node.next = self.right
        node.prev = self.right.prev

        self.right.prev.next = node
        self.right.prev = node

        # the node is now inserted. at the rightmost side of the linked list
        # now we put it in our dictionary.

        self.cache[node.key] = node

        


    def remove(self, node):
        next = node.next
        previous = node.prev

        next.prev = previous
        previous.next = next





    def get(self, key: int) -> int:
        # gets the node we are looking for. 
        # if it isn't there we return 1

        if key in self.cache:
            # the hashmap is used as a pointer to access any node
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        
        else:
            return -1








        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        newNode = Node(key, value)
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
