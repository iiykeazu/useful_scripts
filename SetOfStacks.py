class Node():
    def __init__(self,value):
        self.value = value
        self.above = None
        self.below = None

class Stack():
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0

    def isEmpty(self):
        print(self.size)
        return self.size == 0
    def isFull(self):
        return self.size == self.capacity

    def join(self, above, below):
        if above != None:
            above.below = below
        if below != None:
            below.above = above

    def push(self, value):
        n = Node(value)
        if self.size < self.capacity:
            self.join(n, self.top)
            self.top = n
            if self.size == 0:
                self.bottom = n
            self.size += 1
            return True
        else:
            return False

    def pop(self):
        if self.size == 0:
            raise Exception("This Stack is empty fool")
        else:
            value = self.top.value
            self.top = self.top.below
            if self.top == None:
                self.bottom = None
            else:
                self.top.above = None
            self.size -= 1
            return value

    def removeBottom(self):
        b = self.bottom
        self.bottom = b.above
        if self.bottom != None:
            self.bottom.below = None
        self.size -= 1
        return b.value

    def printStack(self):
        curr = self.bottom
        lst = []
        while curr != None:
            lst.append(curr.value)
            curr = curr.above
        print(lst)

class SetOfStacks():
    def __init__(self, capacity):
        self.__list = []
        self.__capacity = capacity

    def getLastStack(self):
        if len(self.__list) == 0:
            return None
        return self.__list[-1]

    def push(self, value):
        last = self.getLastStack()
        if last == None or last.isFull():
            last = Stack(self.__capacity)
            self.__list.append(last)
        last.push(value)

    def pop(self):
        last = self.getLastStack()
        if last == None or last.isEmpty():
            raise Exception("This set has no stack")
        else:
            value = last.pop()
            if last.isEmpty():
                self.__list.remove(last)
            return value

    def popAt(self, index):
        if index<0 or index>=len(self.__list):
            raise Exception("Index out of bounds")
        return self.leftShift(index, True)

    def leftShift(self, index, removeTop):
        removed_item = None
        stack = self.__list[index]
        if removeTop:
            removed_item = stack.pop()
        else:
            removed_item = stack.removeBottom()
        if stack.isEmpty():
            print("Not this")
            self.__list.remove(stack)
        elif index+1 < len(self.__list):
            newTop = self.leftShift(index+1,False)
            stack.push(newTop)
        return removed_item

    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

    def printSet(self):
        print(self.__list)
        for i in range(len(self.__list)):
            print(i)
            print(self.__list[i].printStack())
