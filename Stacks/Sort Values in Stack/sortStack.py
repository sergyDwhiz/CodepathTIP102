'''
Thought process:
1. Pop elements from Stack into an Array,
2. Sort array
3. Reverse order.
4. Push elements back into stack
'''

from Stack import MyStack

def sort_stack(stack):
    '''
    Thought process:
    1. Pop elements from Stack into an Array
    2. Sort array
    3. Reverse order
    4. Push elements back into stack
    '''
    temp = []

    # Step 1: Pop elements from Stack into an Array
    while not stack.is_empty():
        temp.append(stack.pop())

    # Step 2: Sort array
    temp.sort()

    # Step 3: Reverse order
    temp.reverse()

    # Step 4: Push elements back into stack
    for item in temp:
        stack.push(item)

    return stack

# Example usage:
stack = MyStack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(2)

sorted_stack = sort_stack(stack)
while not sorted_stack.is_empty():
    print(sorted_stack.pop())  # Output: 1 2 3 4