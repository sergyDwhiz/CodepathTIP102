from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max = 0
        for prices in prices:
            if prices < min:
                min = prices
            elif prices - min > max:
                max = prices - min
        return max

