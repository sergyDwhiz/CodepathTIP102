def find_nth(head, n):

    result = head # This iterator will reach the Nth node
    end = head  # This iterator will reach the end of the list

    count = 0
    while count < n:
        end = end.next
        count += 1

    while end is not None:
        end = end.next
        result = result.next

    return result