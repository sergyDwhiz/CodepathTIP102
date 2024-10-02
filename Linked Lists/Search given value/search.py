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


## Recursive Approach
def search(head, value):
    current_node = head
    return searchRecursive(current_node, value)

def searchRecursive(node, value):
    if(not node):
        return False
    if(node.data == value):
        return True
    # Recursively call next node in list
    return searchRecursive(node.next, value)
