class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

   

    def push(self, x: int) -> None:
        self.in_stack.append(x)
    

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not  self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    s1 = MyQueue()
    s1.push(1)
    s1.push(2)
    print(s1.peek())   # expected 1
    print(s1.pop())    # expected 1
    print(s1.empty())  # expected False