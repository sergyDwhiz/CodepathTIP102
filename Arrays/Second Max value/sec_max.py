def find_second_maximum(nums):
    first_max = sec_max = float('-inf')
    for i in range(len(nums)):
      if (nums[i] > first_max):
        sec_max = first_max
        first_max = nums[i]

      elif (nums[i] > sec_max and nums[i]!= first_max):
        sec_max = nums[i]

    return sec_max

