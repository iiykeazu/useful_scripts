class QwStacks():
    def __init__(self):
        self.__stackA = []
        self.__stackB = []

    def atob(self):
        while len(self.__stackA)>0:
            self.__stackB.append(self.__stackA.pop())

    def size(self):
        return len(self.__stackA) + len(self.__stackB)

    def add(self,item):
        self.__stackA.append(item)

    def remove(self, item):
        if len(self.__stackB) == 0:
            self.atob()
        return self.__stackB.pop()

    def peek(self):
        if len(self.__stackB) == 0:
            self.atob()
        return self.__stackB[-1]

    def isEmpty(self):
        return self.size() == 0
