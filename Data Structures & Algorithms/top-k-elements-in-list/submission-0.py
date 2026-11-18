import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use a heap
        # if another number has greater frequency in hashmap frequency list -> pop from heap if len(heap) <= 2

        k_num = [nums[1]]

        for i in nums:
            if i > k_num[1]:
                heapq.heappop(k_num,k_num[1])
                heapq.heapush(k_num,i)
            if len(heapq) > 2:
                heapq.heappop(k_num, 1)
            



        

