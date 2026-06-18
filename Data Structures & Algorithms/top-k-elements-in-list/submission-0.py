from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        #bucket sort
        bucket = [[] for _ in range(len(nums)+1)]

        for num, count in hashmap.items():
            bucket[count].append(num)
        
        # collect top k elements
        res=[]
        #iterate backwards in bucket
        for i in range(len(bucket) - 1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
        