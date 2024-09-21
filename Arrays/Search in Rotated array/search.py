class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Check sorted part
            if nums[left] <= nums[mid]:
                # left is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                # right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
