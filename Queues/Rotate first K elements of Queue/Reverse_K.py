from . import MyQueue
from . import MyStack

def reverse_k_elements(queue, k):
    if queue.is_empty():
        return queue  # No rotation can be done on an empty queue

    k = k % len(queue.queue)  # Ensure k is within the bounds of the queue length

    if k == 0:
        return queue  # No need to rotate if k is 0

    stack = MyStack()

    # Dequeue the first k elements and push them onto the stack
    for _ in range(k):
        stack.push(queue.dequeue())

    # Enqueue the elements from the stack back to the queue
    while not stack.is_empty():
        queue.enqueue(stack.pop())

    # Move the remaining elements to the back of the queue
    for _ in range(len(queue.queue) - k):
        queue.enqueue(queue.dequeue())

    return queue