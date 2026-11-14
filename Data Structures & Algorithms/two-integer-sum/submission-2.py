class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = 0
        seen = []
        output = []

        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                output.append(seen.index(complement))
                output.append(i)
            seen.append(x)
        return output