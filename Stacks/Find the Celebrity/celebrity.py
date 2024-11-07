def celebrity(MATRIX):
    N = len(MATRIX)

    # Find a potential candidate
    candidate = 0
    for i in range(1, N):

        if MATRIX[candidate][i] == 1:

            candidate = i

    # verify potential candidate
    # Candidate must ben known by everyone else
    # Candidate myst not know anyone else

    for i in range(N):
        if i != candidate: # compare the candidate with every other element except itself
            if MATRIX[candidate][i] == 1 or MATRIX[i][candidate] == 0: #
                return -1

    return candidate