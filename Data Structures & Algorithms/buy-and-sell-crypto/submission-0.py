class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best = 0
        while right < len(prices):
            best = max(best, (prices[right] - prices[left]))
            if prices[left] < prices[right]:
                right +=1 
            else:
                left +=1
                right +=1 
        return best