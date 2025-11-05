import random
class Queue():
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, self.__list))

    def enqueue(self, e):
        self.__list.append(e)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def first(self):
        if self.is_empty():
            return None
        return self.__list[0]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)

    def generate(self, num, min, max):
        for i in range(num):
            self.enqueue(random.randint(min, max))

class Stack():
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, reversed(self.__list)))

    def push(self, e):
        self.__list.append(e)
        return True

    def pop(self):
        if self.is_empty():
            return "Error no es posible desapilar, no hay elementos"
        return self.__list.pop()

    def top(self):
        if self.is_empty():
            return "Error no es posible leer el tope, no hay elementos"
        return self.__list[-1]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)

    def generate(self, num, min, max):
        for i in range(num):
            self.push(random.randint(min, max))