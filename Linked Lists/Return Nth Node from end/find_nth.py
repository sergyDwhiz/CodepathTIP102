def find_nth(head, n):

    current_node = head
    position = (length(head) - 1) - n + 1

    while position > 0:
        current_node = current_node.next
        position -= 1

    return current_node


def length(head):
    # Start from the first element
    curr = head
    length = 0

    # Traverse the list and count the number of nodes
    while curr is not None:
        length += 1
        curr = curr.next
    return length