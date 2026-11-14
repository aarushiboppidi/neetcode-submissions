class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for each in list numbers
        # check the index of target - number 
        # if that target - number exists in list,
        # add index each and index target-number to a list
        right = len(numbers) -1
        left = 0
        for i in numbers:
            if numbers[right] + numbers[left] > target:
                right -= 1
            if numbers[right] +numbers[left] < target:
                left +=1
            if numbers[right] +numbers[left] == target:
                return [left+1,right+1]

          
            