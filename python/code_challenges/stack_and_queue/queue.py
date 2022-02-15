from node import Node

class Queue:

    def _init_(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.front:
            self.rear.next = Node(value)
            self.rear = self.front

        else:
            self.front = Node(value)
            self.rear = self.front

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        else:
            raise Exception('Queue is Empty')

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise Exception('Queue is empty')

    def is_empty(self):
        return self.front == None




