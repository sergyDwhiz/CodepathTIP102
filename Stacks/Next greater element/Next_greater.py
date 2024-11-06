from Stack import MyStack

def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)

    for i in reversed(range(len(lst))):
        # While stack has elements and the current element is greater
        # than top element, pop all elements
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()

        # If the stack has an element, the top element will be
        # greater than ith element
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])

    return res