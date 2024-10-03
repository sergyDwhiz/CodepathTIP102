# Definition for a linked list node

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_duplicates(head):
    seen = set()
    current = head
    seen.add(current.data)
    if not head:
      return head
    while current and current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
          seen.add(current.next.data)
          current = current.next
    return head