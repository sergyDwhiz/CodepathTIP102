class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def is_palindrome(head):
    start = head
    end = get_tail(head)

    if start is None:
        return True
    while start != end and start.prev!= end:
        if start.data != end.data:
            return False
        start = start.next
        end = end.prev
    return True

def get_tail(head):
    current = head
    while current.next:
        current = current.next
    return current
