class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = len(prices) - 1
        best = 0
        while left < right:
            best = max(best, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left+=1
            else:
                right -=1
        return best