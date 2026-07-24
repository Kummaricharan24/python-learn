class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Driver Code (for VS Code)

q = MyCircularQueue(3)

print(q.enQueue(1))   # True
print(q.enQueue(2))   # True
print(q.enQueue(3))   # True
print(q.enQueue(4))   # False

print(q.Rear())       # 3
print(q.isFull())     # True

print(q.deQueue())    # True

print(q.enQueue(4))   # True

print(q.Rear())       # 4

print("Queue Array :", q.queue)
print("Front Index :", q.front)
print("Rear Index  :", q.rear)
print("Size        :", q.size)