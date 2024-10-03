from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length = len(nums)
		answer = [1] * length

		# Calculate left products
		left_product = 1
		for i in range(length):
			answer[i] = left_product # Store left product in answer array
			left_product = left_product * nums[i] # Update left product with current elt and add to answer array

		# Calculate right products and final result
		right_product = 1
		for i in range(length - 1, -1, -1): # Start from the end of the array
			answer[i] = answer[i] * right_product # Multiply left product with right product
			right_product *= nums[i]

		return answer

