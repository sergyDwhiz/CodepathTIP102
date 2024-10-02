class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(head, value):

    current = head
    while current:
      if current.data == value:
        current.data = None