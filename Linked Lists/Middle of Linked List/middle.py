class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def middle(head):
    if not head or not head.next:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow