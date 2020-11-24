class Animal():
    def __init__(self,name,order):
        self.name = name
        self.order = order
    def isOlderThan(self, animal):
        return self.order <= animal.order

class Dog(Animal):
    def __init__(self,name,order):
        super().__init__(name,order)

class Cat(Animal):
    def __init__(self,name,order):
        super().__init__(name,order)

class AnimalQueue():
    dogs = []
    cats = []
    def __init__(self):
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        if isinstance(animal,Dog):
            dogs.append(animal)
        elif isinstance(animal, Cat):
            cats.append(animal)
        self.order += 1
        return

    def dequeueDog(self):
        return dogs.pop(0)

    def dequeueCat(self):
        return cats.pop(0)

    def dequeueAny(self):
        if len(dogs) == 0:
            return self.dequeueCat()
        elif len(cats) == 0:
            return self.dequeueDog()
        dog = dogs[0]
        cat = cats[0]
        if dog.isOlderThan(cat):
            return self.dequeueDog()
        elif cat.isOlderThan(dog):
            return self.dequeueCat()
