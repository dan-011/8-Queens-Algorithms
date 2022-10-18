from DoublyLinkedList import *

class MyQueue:
    def __init__(self, l = []):
        self.dll = DoublyLinkedList()
        for elem in l:
            self.dll.add_last(elem)

    def __len__(self):
        return len(self.dll)
    
    def enqueue(self, item):
        self.dll.add_first(item)
    
    def dequeue(self):
        return self.dll.rem_last()
    
    def peek(self):
        return self.dll.tail.getVal()

if __name__ == '__main__':
    queue = MyQueue()
    for i in range(10):
        queue.enqueue(i)
    assert(len(queue) == 10)
    for i in range(10):
        assert(i == queue.dequeue())
    assert(len(queue) == 0)