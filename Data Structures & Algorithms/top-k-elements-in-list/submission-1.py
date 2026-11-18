import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use a heap
        # if another number has greater frequency in hashmap frequency list -> pop from heap if len(heap) <= 2

        k_num = []
        freq = {}

        for val in nums:
            freq[val] = freq.get(val, 0) + 1

        for i in freq:
            heapq.heappush(k_num, (freq[i],i))
            if len(k_num) > 2:
                heapq.heappop(k_num) 
            
        return [num for count,num in k_num]
            #two heaps for value vs. freq?


        

