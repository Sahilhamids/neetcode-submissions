class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        val = self.stack.pop(0)
        return val
    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        else:
            return 
    def empty(self) -> bool:
        return True if not self.stack else False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()