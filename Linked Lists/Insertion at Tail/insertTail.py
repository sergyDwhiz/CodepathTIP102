class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_Tail(head, target):
    new_node = LinkedListNode(target)
    # If list is empty, new node becomes head
    if not head:
        return new_node
    # Traverse the list to reach the end
    current = head
    while current.next: # Stop at the last node
        current = current.next  # iterate to the next node

    # Append the new node at the end
    current.next = new_node
    return head