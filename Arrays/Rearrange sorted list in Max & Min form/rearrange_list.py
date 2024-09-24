def rearrange_list(nums):
    if (len(nums) == 0):
        return []

    result = []
    mid = len(nums) // 2

    # Iterate through half of the sorted list
    for i in range(mid):
        # Append the largest remaining element (from the end of the list)
        result.append(nums[-(i+1)])
        # Append the smallest remaining element (from the start of the list)
        result.append(nums[i])

    if len(nums) % 2 == 1:
        result.append(nums[mid])

    return result