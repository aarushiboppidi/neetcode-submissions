class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = 0
        seen = set()
        output = []
        for i in nums:
            complement = target - i
            seen.add(complement)
            if complement in seen:
                output.append(nums.index(i))
                output.append(nums.index(complement))
                break

        return output
