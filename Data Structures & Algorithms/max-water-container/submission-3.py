class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #width = indexright -index left
        #height = min(numsleft, numsright)
        
        left = 0
        right = len(heights) - 1 
        best = 0
        width = 0
        while left < right:
            width = right - left
            water = width * (min(heights[right],heights[left]))
            best = max(best, water)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
            

        return best


