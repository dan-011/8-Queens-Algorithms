class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
    def getVal(self):
        return self.val

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def add_first(self, val):
        new_node = Node(val)
        if(len(self) == 0):
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.len += 1

    def add_last(self, val):
        new_node = Node(val)
        if(len(self) == 0):
            self.add_first(val)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.len += 1
    
    def get_first(self):
        if(len(self) == 0):
            raise IndexError("Cannot get first from empty dll")
        else:
            return self.head.getVal()
    
    def get_last(self):
        if(len(self) == 0):
            raise IndexError("Cannot get last from empty dll")
        else:
            return self.tail.getVal()

    def rem_first(self):
        if(len(self) == 0):
            raise IndexError("Cannot remove first from empty dll")
        elif(len(self) == 1):
            val = self.head.getVal()
            self.head = None
            self.tail = None
            self.len -= 1
            return val
        else:
            val = self.head.getVal()
            self.head = self.head.next
            self.head.prev = None
            self.len -= 1
            return val
    
    def rem_last(self):
        if(len(self) == 0):
            raise IndexError("Cannot remove last from empty dll")
        elif(len(self) == 1):
            val = self.head.getVal()
            self.head = None
            self.tail = None
            self.len -= 1
            return val
        else:
            val = self.tail.getVal()
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
            return val
            
if __name__ == '__main__':
    dll = DoublyLinkedList()
    for i in range(10):
        dll.add_last(i)
    assert(len(dll) == 10)
    node = dll.head
    val = 0
    while(node is not None):
        assert(node.getVal() == val)
        val += 1
        node = node.next
    node = dll.tail
    val = len(dll) - 1
    while(node is not None):
        assert(node.getVal() == val)
        val -= 1
        node = node.prev

    for i in range(10):
        v = dll.rem_first()
        assert(v == i)
    
    assert(len(dll) == 0)

    for i in range(9, -1, -1):
        dll.add_first(i)
    
    assert(len(dll) == 10)
    node = dll.head
    val = 0
    while(node is not None):
        assert(node.getVal() == val)
        val += 1
        node = node.next
    node = dll.tail
    val = len(dll) - 1
    while(node is not None):
        assert(node.getVal() == val)
        val -= 1
        node = node.prev

    for i in range(-9, -1, -1):
        v = dll.rem_last()
        assert(v == i)