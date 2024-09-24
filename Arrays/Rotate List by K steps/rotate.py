def rotate(nums, k):
    if len(nums) == 0:
        k = 0 # No rotation can be done on an empty list
    else:
        k = k % len(nums)

    rotated_list = nums[-k:] + nums[:-k] # append last 'k'th elements to list start and
    # all other element from start of list to last 'k'th elements.