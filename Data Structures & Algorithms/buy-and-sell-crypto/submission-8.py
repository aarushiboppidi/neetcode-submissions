class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best = 0
        while right<len(prices):
            if prices[left] < prices[right]:
                best = max(best, prices[right] - prices[left])
                right+=1
            else:
                left = right
                left +=1
        return best