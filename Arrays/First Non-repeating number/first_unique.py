def first_unique(nums):
    seen = {}
    for i in nums:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    for i in nums:
        if seen[i] == 1:
            return i

    return -1