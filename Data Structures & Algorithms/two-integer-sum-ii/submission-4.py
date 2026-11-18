class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for each in list numbers
        # check the index of target - number 
        # if that target - number exists in list,
        # add index each and index target-number to a list

        for i, each in enumerate(numbers):
            need = target - each
            if need in numbers and i < numbers.index(need):
                return [numbers.index(each)+1, numbers.index(need)+1]
          
            