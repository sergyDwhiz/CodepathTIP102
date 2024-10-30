class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        # Increment top pointer and add element to stack 1 if space is available, else print stack overflow and exit
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print("Stack Overflow ")
            exit(1)

    def push2(self, value):
        # Decrement top pointer and add element to stack 2 if space is available, else print stack overflow and exit
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print("Stack Overflow ")
            exit(1)

    def pop1(self):
        # Return and remove top element from stack 1 if not empty, else print stack underflow and exit
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        # Return and remove top element from stack 2 if not empty, else print stack underflow and exit
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack Underflow ")
            exit()