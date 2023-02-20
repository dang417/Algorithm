class Queue:
    def __init__(self, n):
        self.size = n           # 전체 크기
        self.items = [None]     # 각 아이템
        self.rear = -1          # rear
        self.front = -1         # front

    def enQueue(self, item):
        if self.isFull():
            print('isFull')
        else:
            self.rear += (self.rear + 1) % self.size
            self.items[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print('is Empty')
        else:
            self.front += 1
            item = self.items[self.front]
            self.items[self.front] = None
            return item

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return  self.rear == self.size -1

    def Peek(self):
        return  self.items[self.front]

q = Queue(4)
print(q.items)
q.enQueue('A')
q.enQueue('B')
print(q.items)
print(q.front)
print(q.isEmpty())
print(q.deQueue())
print(q.items)
print(q.front)
print(q.deQueue())
print(q.isEmpty())
print(q.items)
q.enQueue('C')
q.enQueue('D')
print(q.items)
print(q.deQueue())
print(q.deQueue())
print(q.items)
print(q.isEmpty())
print(q.isFull())
