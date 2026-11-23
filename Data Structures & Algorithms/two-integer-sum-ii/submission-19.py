class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = 1
        seen = set()
        if numbers[left] + numbers[right] > target:
            return []

        while left < right and right < len(numbers)-1:
            if numbers[left] + numbers[right] < target:
                left += 1
            right +=1
        return [left+1, right+1]
    

          
            