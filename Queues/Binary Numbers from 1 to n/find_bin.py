from queue import Queue


def find_bin(n):
    result = []
    queue = Queue()

        # Start with '1' in the queue
    queue.enqueue(1)

        # Loop to generate binary numbers up to 'n'
    for i in range(n):
        # Dequeue the front element of the queue, convert it to string and append it to the result list
        result.append(str(queue.dequeue()))

        # Generate new binary numbers by appending '0' and '1' to the dequeued number
        s1 = result[i] + "0"
        s2 = result[i] + "1"

        # Enqueue the new binary numbers back into the queue
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result
