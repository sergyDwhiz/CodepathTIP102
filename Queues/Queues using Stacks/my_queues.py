from Stack import MyStack
class NewQueue:
    def __init__(self): #
        self.main_stack = MyStack()
        self.temp_stack = MyStack()


    # Insert elements in the Queue
    def enqueue(self, value):
        # If main_stack and temp_stack is empty, push value into it.
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
        else:
            # if main stack is not empty, empty its contents into temp stack
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # since main_stack is now empty, you can now push the values back to it.
            self.main_stack.push(value)
            # While temp_stack is not empty, pop its elements and move them to main stack (Main Queue operation)

            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    def dequeue(self):
        # return a value from main_stack if not empty.
        if self.main_stack.is_empty():
            return None
        else:
            value = self.main_stack.pop()
        return value

    # Time complexity for enqueue operation is O(n), since it will take "n" time to move elts to main_stack and back
    # Time complexity for dequeue is O(1), or constant time, because we point to the top of the queue, so we just pop the first elt.

