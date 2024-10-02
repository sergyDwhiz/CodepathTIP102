class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False