class Stack:
    def __init__(self, l = []):
        self.l = l
    
    def __len__(self):
        return len(self.l)

    def push(self, item):
        self.l.append(item)
    
    def pop(self):
        if len(self) == 0:
            raise IndexError("Cannot pop from empty stack")
        item = self.l.pop()
        return item
    
    def peek(self):
        if len(self) == 0:
            raise IndexError("Cannot peek on empty stack")
        return self.l[-1]