class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack():
    def __init__(self):
        self.stack = None
        self.minStack = None
        self.min = None
        self.size = 0

    def pop(self):
        if self.size == 0:
            print("Stop It")
            return
        else:
            data = self.stack.data
            self.stack = self.stack.next
            self.minStack = self.minStack.next if data == self.min else self.minStack
            self.size -= 1
            if self.size > 0:
                self.min = self.minStack.data
            else:
                self.min = None
            return data

    def push(self, data):
        n = Node(data)
        n.next = self.stack
        self.stack = n
        self.size += 1
        if self.size == 1 or data < self.min:
            n = Node(data)
            n.next = self.minStack
            self.minStack = n
            self.min = data

    def peek(self):
        if self.size == 0:
            print("Stop It")
            return
        else:
            return self.stack.data

    def minim(self):
        return self.min

    def isEmpty(self):
        return self.size == 0
