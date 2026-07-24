class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k
        self.last = -1
        self.front = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.last = (self.last + 1) % self.capacity
        self.deque[self.last] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.last = (self.last - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.deque[self.last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# ---------------- Driver Code ----------------

dq = MyCircularDeque(3)

print(dq.insertLast(1))     # True
print(dq.insertLast(2))     # True
print(dq.insertFront(3))    # True
print(dq.insertFront(4))    # False

print(dq.getRear())         # 2
print(dq.isFull())          # True

print(dq.deleteLast())      # True

print(dq.insertFront(4))    # True

print(dq.getFront())        # 4

print("Deque :", dq.deque)
print("Front :", dq.front)
print("Last  :", dq.last)
print("Size  :", dq.size)