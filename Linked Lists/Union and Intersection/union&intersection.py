from linked_list_operations import LinkedListNode, intersection


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def union(head1, head2):
    # Create new set to store united elements
    new = set()

    # Traverse list one and add elements
    current1 = head1
    while current1:
        new.add(current1.data)
        current1 = current1.next

    # Traverse list two and add elements
    current2 = head2
    while current2:
        new.add(current2.data)
        current2 = current2.next

    return new

def intersection(head1, head2):
    # Create sets to store elements of both lists
    set1 = set()
    set2 = set()

    # Traverse the first list and add each element to set1
    current1 = head1
    while current1:
        set1.add(current1.data)
        current1 = current1.next

    # Traverse the second list and add each element to set2
    current2 = head2
    while current2:
        set2.add(current2.data)
        current2 = current2.next

    # Find the intersection of both sets
    intersection_set = set1.intersection(set2)

    return intersection_set

