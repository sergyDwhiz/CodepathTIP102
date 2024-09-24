def find_second_maximum(nums):

    nums.sort()
    length = len(nums)
    if nums[-1] == nums [-2]:
      return nums[-3]
    else:
      return nums[-2]

