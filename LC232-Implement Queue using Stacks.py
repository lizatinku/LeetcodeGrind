# My plan
# Have 2 stacks - stack 1 for incoming elements and stack 2 for outgoing elements
# Push new elements from the queue into stack 1
# Pop operation
#   as an edge case, check if stack 2 is empty
#   pop the element from stack 1 and push into stack 2
# Peek operation
#   Transfer elements from s1 to s2 if s2 is empty
#   after popping, access the top element of s2 without removing it.
# if both stack 1 and stack 2 are empty, return true
# else, return false

# Concepts:
# Stack: DSA that follows a Last In, First Out (LIFO) principle. Elements are added and removed from the top of the stack.
# Queue: DSA that follows a First In, First Out(FIFO) principle. Elements are added to the back and removed from the front.
# Transfering between stacks: helps to maintain the order of elements for different operations.

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0  #to determine if both stacks are empty


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
