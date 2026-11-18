class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for i in nums:
            if i in check:
                return false
            else:
                check.add(i)

        return true
            
