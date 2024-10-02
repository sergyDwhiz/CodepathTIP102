class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head
# Time complexity: O(n)