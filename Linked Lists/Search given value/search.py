class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def searchList(head, value):

    current = head
    while current:
        if current.data == value:
            return True
        current = current.next
    return False
