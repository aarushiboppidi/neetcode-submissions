class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the array
        # one pointer left and one pointer right
        # if pointer left = number before it, add
        # if pointer right = number before it, subtract
        # loop is for loop of all the numbers
        # if right + current num + left is > 0, move right down
        # if right + current num + left < 0, move left up
        # if == 0, add to list

        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        output = []
        for i in range(len(nums)-1):
            while left < right:
                if left>2 and nums[left-1] == nums[left]:
                    left += 1
                elif nums[right] + nums[i] + nums[left] < 0:
                    left += 1
                if nums[right] == nums[right-1]:
                    right-=1
                elif nums[right] + nums[i] + nums[left] > 0:
                    right -=1
                else:
                    output.append([nums[i],nums[left],nums[right]])

        return output

                    