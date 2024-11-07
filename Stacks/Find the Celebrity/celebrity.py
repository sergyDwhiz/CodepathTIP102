def celebrity(MATRIX):
    N = len(MATRIX)

    # Find a potential candidate
    candidate = 0
    for i in range(1, N):
        if MATRIX[candidate][i] == 1:
            candidate = i

    # Verify potential candidate using stacks
    stack = []
    for i in range(N):
        if i != candidate:
            stack.append(i)

    while len(stack) > 0:
        person = stack.pop()

        # If the potential candidate knows the person, or the person doesn't know the potential candidate,
        # then the potential candidate is not a celebrity
        if MATRIX[candidate][person] == 1 or MATRIX[person][candidate] == 0:
            return -1

    return candidate

# Time: O(n^2)
# Space: O(n)