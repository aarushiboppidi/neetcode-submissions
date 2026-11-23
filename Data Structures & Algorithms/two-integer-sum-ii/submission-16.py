class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        seen = set()

        for i in range(1,len(numbers)-1):
            if numbers[left] + numbers[i] > target:
                return []
            elif numbers[left] + numbers[i] < target:
                left += 1
            elif numbers[left]+numbers[i] == target:
                return [left+1, i+1]
    

          
            